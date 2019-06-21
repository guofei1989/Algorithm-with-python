"""
基于栈结构实现简单的()匹配
"""
from pythonds.basic.stack import Stack


def bracketChecker(symbolString):
    s = Stack()    # 采用栈结构存放弹出的括号
    balanced = True
    for index in range(len(symbolString)):
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)

        else:
            if s.isEmpty():     # ")"数量大于“(”
                balanced = False
                break
            else:
                s.pop()      # 弹出与")"对应的“(”

    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(bracketChecker("((()))"))
    print(bracketChecker("(()"))
