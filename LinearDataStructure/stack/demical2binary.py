"""
利用栈进行十进制到二进制的转换
"""
from pythonds.basic.stack import Stack


def dem2bin(value):
    s = Stack()
    result = ""
    while value != 0:
        mod = value % 2
        s.push(mod)
        value = value // 2
    while not s.isEmpty():
        result += str(s.pop())
    return result


if __name__ == '__main__':
    print(dem2bin(10))
    print(dem2bin(135))
