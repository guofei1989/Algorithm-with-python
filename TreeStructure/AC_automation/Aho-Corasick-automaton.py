"""
自己实现AC自动机：Trie树+KMP+失配指针
"""


# Trie树节点
class Node(object):
    def __init__(self):
        self.children = {}    # {value: Node()}
        self.tail = False     # 是否为string tail标记
        self.word = ""     # 保存string
        self.fail = None   # 失配指针, 类似于KMP算法中next数组值


class AC_Automation(object):
    def __init__(self):
        self.root = Node()
        self.count = 0  # 模式串个数

    # Trie树添加word
    def add(self, word):
        self.count += 1
        curNode = self.root
        for w in word:
            if w not in curNode.children.keys():
                curNode.children[w] = Node()   # 增加新的Node
            curNode = curNode.children.get(w)

        curNode.tail = True    # 词尾标记
        curNode.word = word    # 存储word

    # 利用BFS遍历Trie树，建立失配指针
    def make_fail(self):
        node_queue = []    # Node序列
        node_queue.append(self.root)
        while node_queue:
            temp_node = node_queue.pop(0)
            for key, value in temp_node.children.items():
                if temp_node == self.root:      #根节点孩子们的fail都指向根
                    temp_node.children[key].fail = self.root
                else:
                    p = temp_node.fail
                    while p:    # 递归回溯
                        if key in p.children.keys():
                            value.fail = p.fail
                            break
                        p = p.fail

                    if not p:
                        value.fail = self.root   # 指向根结点

                node_queue.append(value)   # 更新节点孩子们的Node

    # TODO: AC自动机的搜索


if __name__ == '__main__':
    ac = AC_Automation()
    ac.add("aa")
    ac.add("bb")
    ac.add("abb")
    ac.make_fail()



