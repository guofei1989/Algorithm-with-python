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
            if j == Lop:
                print("存在匹配字符串, 对应字符串位置为{}~{}".format(i - j, i-1))
                return
        else:
            j = 0
            i = i - (j-1)

    print("不存在匹配字符串")


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
            if p[j] != p[k]:
                NextArray.append(k)
            else:
                NextArray.append(NextArray.__getitem__(k))
        else:
            k = NextArray[k]
    return NextArray



def KmpSearch(s, p):
    Los = len(s)
    Lop = len(p)

    i = 0     # String指针
    j = 0     # Pattern

    NextArray = GetNext(p)

    while i < Los and j < Lop:
        if j == -1 or s[i] == p[j]:
            j += 1
            i += 1
            if j == Lop:
                print("存在匹配字符串, 对应字符串位置为{}~{}".format(i - j, i-1))
                return

        else:
            j = NextArray.__getitem__(j)

    print("不存在匹配字符串")


if __name__ == '__main__':
    s4test = "BBC ABCDAB ABCDABCDABDE"
    p4test = "BBC"
    # res = ViolentMatch(s4test, p4test)
    # print(res)
    # print(GetNext("abab"))

    KmpSearch(s4test, p4test)