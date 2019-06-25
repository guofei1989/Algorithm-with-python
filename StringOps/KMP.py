"""
KMP算法常用来进行在一个文本串S内查找一个模式串P 的出现位置
S:字符串string
P:匹配串pattern

相较于暴力匹配（见ViolentMatch）每次匹配失败S必须进行回溯，KMP通过计算P中子串的next数组可快速定位到pattern回溯的位置
next数组和前缀后缀最长公共元素长度间的关系

"""


def ViolentMatch(s, p):
    # 暴力匹配
    Los = len(s)
    Lop = len(p)

    i = 0   # 记录string位置
    j = 0   # 记录pattern位置
    while i < Los and j < Lop:
        if s[i] == p[j]:
            i += 1
            j += 1

        else:
            j = 0
            i = i - (j-1)

    if j == Lop:
        return "存在匹配字符串"
    else:
        return "不存在匹配字符串"


def GetNext(p):
    # 递推获得next数组
    NextArray = []
    NextArray.append(-1)    # 设定初值
    k = -1   # next数组元素变量
    j = 0    # next数组指针
    while j < len(p) - 1:

        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            NextArray.append(k)
        else:
            k = NextArray[k]
    return NextArray





if __name__ == '__main__':
    s4test = "BBC ABCDAB ABCDABCDABDE"
    p4test = "ABCDABD"
    # res = ViolentMatch(s4test, p4test)
    # print(res)
    print(GetNext("ABCDABD"))