"""
验证列表在递归操作中的变化
列表result_list虽然在每层都令为[]，但递归会会做append
"""


def sum(NumberList):
    result_list = []
    if len(NumberList) == 1:
        result_list.append(NumberList[0])
    else:
        result_list.extend([NumberList[0], sum(NumberList[1:])])
    return result_list


if __name__ == '__main__':
    res = sum([1, 3, 5, 7, 9])
    print(res)
