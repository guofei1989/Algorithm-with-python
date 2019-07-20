"""
strA——>strB
len(strA)=I,len(strB)=J

空字符串长度为0
ED[i][j]=0, i=0,j=0
ED[i][j]=j, i=0, J>=j>0
ED[i][j]=j, j=0, I>=i>0
ED[i][j]=min{ED[i-1][j]+1,ED[i][j-1]+1,ED[i-1][j-1]+flag}   flag={ED[i]=ED[j]:1, ED[i]!=ED[j]:0}
通过动态规划的方式计算ED矩阵

ED[i-1][j]+1表示删除字符，ED[i][j-1]+1表示添加字符， ED[i-1][j-1]+flag表示修改字符
"""


import numpy as np


class EditDistance(object):
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

    def _generate_ED_matrix(self):
        lenA = len(self.strA)
        lenB = len(self.strB)
        ED_matrix = np.zeros((lenA + 1, lenB + 1))

        ED_matrix = np.zeros((lenA + 1, lenB + 1))

        # 初始值
        ED_matrix[0][0] = 0  # A、B均为空
        for j in range(1, lenB + 1):
            ED_matrix[0][j] = j  # A空，B不空，做添加操作

        for i in range(1, lenA + 1):
            ED_matrix[i][0] = i  # A不空，B空，做删除操作

        # 动态规划
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                edit_del_distance = ED_matrix[i - 1][j] + 1  # 删除操作
                edit_add_distance = ED_matrix[i][j - 1] + 1  # 添加操作

                flag = 0 if self.strA[i - 1] == self.strB[j - 1] else 1
                edit_alter_distance = ED_matrix[i - 1][j - 1] + flag

                ED_matrix[i][j] = min(edit_del_distance, edit_add_distance, edit_alter_distance)

        return ED_matrix

    def similarity(self):
        ED_matrix = self._generate_ED_matrix()
        edit_distance = ED_matrix[-1][-1]
        sim = 1 - edit_distance/max(len(self.strA), len(self.strB))
        return sim


if __name__ == '__main__':
    A = "godfliy"
    B = "godfrey"
    ed = EditDistance(A, B)
    sim = ed.similarity()
    print(sim)
