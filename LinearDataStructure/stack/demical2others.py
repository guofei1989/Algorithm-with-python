"""
利用栈进行十进制到其他进制（二进制 ~ 十六进制）的转换
"""
from pythonds.basic.stack import Stack


def dem2base(value, base):
    flag = "0123456789ABCDEF"
    s = Stack()
    result = ""
    while value != 0:
        mod = flag[value % base]
        s.push(mod)
        value = value // base
    while not s.isEmpty():
        result += str(s.pop())
    return result


if __name__ == '__main__':
    print(dem2base(10, 2))
    print(dem2base(935, 16))
