"""
基于列表实现栈
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        """栈顶添加元素"""
        self.items.append(item)

    def pop(self):
        """栈顶弹出元素"""
        return self.items.pop()

    def peek(self):
        """get栈顶元素"""
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push('cat')
    stack.push(4)
    print(stack.peek())
    print(stack.size())
    print(stack.pop())
    print(stack.size())
