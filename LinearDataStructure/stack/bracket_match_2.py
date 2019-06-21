"""
基于栈结构实现复杂的()、[]和{}的匹配
"""
from pythonds.basic.stack import Stack


def bracketChecker(symbolString):
    s = Stack()    # 采用栈结构存放弹出的括号
    balanced = True
    for index in range(len(symbolString)):
        symbol = symbolString[index]
        if symbol in ["(", "[", "{"]:
            s.push(symbol)

        else:
            if s.isEmpty():     # ")"数量大于“(”
                balanced = False
                break
            else:
                top = s.pop()      # 弹出与")"对应的“(”
                if matches(top, symbol):     # 通过一个外置函数实现对应符号的匹配，也可以穷举-判断
                    continue
                else:
                    balanced = False
                    break
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    return "([{".index(open) == ")]}".index(close)


if __name__ == '__main__':
    print(bracketChecker("{[]([]())}"))
    print(bracketChecker("({()"))
