"""
医学中常用的生存曲线
"""
import pandas as pd
import random
import matplotlib.pyplot as plt


def generate_data():
    num = 200    # 数据长度
    df = pd.DataFrame({"ID": range(1, num+1), "Life":[random.randint(1, 100) for _ in range(num)],
                       "Status": [random.choice([0, 1]) for _ in range(num)]})

    df_tmp = df.sort_values(by=["Life", "Status"])
    df_tmp.to_excel('survival_test.xlsx')

    return df


def compare_data():
    # 数据来源于 http://www.360doc.com/content/17/0626/11/6175644_666623573.shtml
    df = pd.DataFrame({"Life": [1.5, 2.7, 3.1, 3.2, 4.1, 4.5, 4.8, 5.1, 6.2, 6.7, 7.5, 8.8],
                       "Status": [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]})
    return df


def generate_Kaplan_Meier(df, missing=True):
    data = df.sort_values(by="Life")   # 根据寿命排序
    max_life = max(df["Life"])      # 最大寿命
    life_list = []    # 生命值拐点序列
    survival_rate = []      # 生存概率序列

    patient_survival_X = []    # 失访患者的X数据
    patient_survival_Y = []    # 失访患者的Y数据

    patient_count = len(data)    # 所有患者的数量
    patient_followup_total = patient_count   # 记录每个时间段仍进行随访的患者数量, 这里是初值
    patient_followup_survival = patient_count   # 记录每个时间段仍进行随访的患者中存活的数量，这里是初值

    life_list.append(0)    # 时间初值
    survival_rate.append(1)    # 生存率初值

    life_list.extend(data[data['Status']==1]['Life'].unique())   # 补充所有的时间序列节点

    for i, j in enumerate(life_list):   # 统计死亡周期内的数据
        if i == 0:
            continue
        patient_dead_num = len(data[(data['Life']==j)&(data['Status']==1)])    # 在该阶段死亡的患者数量, Status=1表示死亡, 0表示未死亡或失访
        patient_missing = data[(data['Life']<=j)&(data['Life']>life_list[i-1])&(data['Status']==0)]   # type:pd.DataFrame()
        patient_missing_num = len(patient_missing)  # 该阶段失访的患者数量

        patient_missing_life = patient_missing['Life'].tolist()
        patient_missing_survivalrate = [survival_rate[i-1]] * patient_missing_num
        patient_survival_X.extend(patient_missing_life)
        patient_survival_Y.extend(patient_missing_survivalrate)

        patient_followup_total -= patient_missing_num     # 此阶段还剩下的随访患者总数（删除失访人数）
        patient_followup_survival -= (patient_missing_num+patient_dead_num)     # 此阶段还剩下的存活患者总数（）

        survival_rate_tmp = patient_followup_survival/patient_followup_total
        survival_rate.append(survival_rate_tmp*survival_rate[i-1])    # 概率累乘

        patient_followup_total -= patient_dead_num   # 下一阶段统计的时候要先去掉此阶段的死亡患者数量

    if life_list[-1] < max_life:    # 补充最后一段数据
        resident_missing_life = data[(data['Life']>life_list[-1])&(data['Status']==0)]
        life_list.append(max_life)   # 最终点的横坐标
        survival_rate.append(survival_rate[-1])     # 最终点的纵坐标
        patient_survival_X.extend(resident_missing_life['Life'].tolist())   # 补充最后一段的横坐标
        patient_survival_Y.extend([survival_rate[-1]]*len(resident_missing_life))

    if missing:
        plt.step(life_list, survival_rate, where='post')
        plt.scatter(patient_survival_X, patient_survival_Y, marker='x')
        plt.ylim(0.0, 1.05)
        plt.show()
        return life_list, survival_rate, patient_survival_X, patient_survival_Y

    else:
        plt.step(life_list, survival_rate, where='post')
        plt.ylim(0.0, 1.05)
        plt.show()
        return life_list, survival_rate


# 对上述功能进行类的封装
class KaplanMeierHandler(object):
    def __init__(self, missing=True):
        """
        :param missing: 是否需要处理失访数据
        """
        self._life_data = None    # 载入的寿命数据
        self._status_data = None    # 载入的状态数据
        self._life_list = []    # 生命值拐点序列
        self._survival_rate = []      # 生存概率序列

        self.missing = missing

        if missing:
            self._patient_survival_X = []    # 失访患者的X数据
            self._patient_survival_Y = []    # 失访患者的Y数据

    def fit(self, x, y):
        """
        :param x: 载入数据的life列
        :param y: 载入数据的status列
        :return: self
        """
        df = pd.DataFrame(pd.concat([pd.Series(x), pd.Series(y)], axis=1), columns=['Life', 'Status'])
        data = df.sort_values(by="Life")  # 根据寿命排序

        max_life = max(data['Life'])  # 最大寿命
        patient_count = len(data)  # 所有患者的数量
        patient_followup_total = patient_count  # 记录每个时间段仍进行随访的患者数量, 这里是初值
        patient_followup_survival = patient_count  # 记录每个时间段仍进行随访的患者中存活的数量，这里是初值
        self._life_list.append(0)  # 时间初值
        self._survival_rate.append(1)  # 生存率初值

        self._life_list.extend(data[data['Status'] == 1]['Life'].unique())  # 补充所有的时间序列节点

        for i, j in enumerate(self._life_list):  # 统计死亡周期内的数据
            if i == 0:
                continue
            patient_dead_num = len(
                data[(data['Life'] == j) & (data['Status'] == 1)])  # 在该阶段死亡的患者数量, Status=1表示死亡, 0表示未死亡或失访
            patient_missing = data[
                (data['Life'] <= j) & (data['Life'] > self._life_list[i - 1]) & (data['Status'] == 0)]  # type:pd.DataFrame()
            patient_missing_num = len(patient_missing)  # 该阶段失访的患者数量

            if self.missing:
                patient_missing_life = patient_missing['Life'].tolist()
                patient_missing_survivalrate = [self._survival_rate[i - 1]] * patient_missing_num
                self._patient_survival_X.extend(patient_missing_life)
                self._patient_survival_Y.extend(patient_missing_survivalrate)

            patient_followup_total -= patient_missing_num  # 此阶段还剩下的随访患者总数（删除失访人数）
            patient_followup_survival -= (patient_missing_num + patient_dead_num)  # 此阶段还剩下的存活患者总数（）

            survival_rate_tmp = patient_followup_survival / patient_followup_total
            self._survival_rate.append(survival_rate_tmp * self._survival_rate[i - 1])  # 概率累乘

            patient_followup_total -= patient_dead_num  # 下一阶段统计的时候要先去掉此阶段的死亡患者数量

        if self._life_list[-1] < max_life:  # 补充最后一段数据
            resident_missing_life = data[(data['Life'] > self._life_list[-1]) & (data['Status'] == 0)]
            self._life_list.append(max_life)  # 最终点的横坐标
            self._survival_rate.append(self._survival_rate[-1])  # 最终点的纵坐标

            if self.missing:
                self._patient_survival_X.extend(resident_missing_life['Life'].tolist())  # 补充最后一段的横坐标
                self._patient_survival_Y.extend([self._survival_rate[-1]] * len(resident_missing_life))

        return self

    def plot(self):
        if self.missing:
            plt.step(self._life_list, self._survival_rate, where='post')
            plt.scatter(self._patient_survival_X, self._patient_survival_Y, marker='x')
            plt.ylim(0.0, 1.05)
            plt.show()
        else:
            plt.step(self._life_list, self._survival_rate, where='post')
            plt.ylim(0.0, 1.05)
            plt.show()


if __name__ == '__main__':
    # data = generate_data()
    data = compare_data()

    handler = KaplanMeierHandler(missing=False)
    handler.fit(data['Life'], data['Status'])
    handler.plot()










