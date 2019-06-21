"""
字典树（Trie): 使用类继承得到
"""


class TrieNode(object):
    # TrieNode有两个成员变量，一个为后续TrieNode，一个是是否为记录当前节点node是否
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        insert a word into the trie
        :type word: str
        :rtype: void
        """
        curNode = self.root

        for c in word:
            if c not in curNode.children.keys():
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for c in word:
            if c not in curNode.children.keys():
                return False
            curNode = curNode.children.get(c)

        return curNode.isWord

    def startswith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for c in prefix:
            if c not in curNode.children.keys():
                return False
            curNode = curNode.children.get(c)

        return True

    def findall(self, prefix):
        """
        Returns all words in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: list of suited words
        """

        def _get_key(pre, pre_node):
            # 递归
            word_list = []
            if pre_node.isWord:
                word_list.append(pre)
            for key in pre_node.children.keys():
                word_list.extend(_get_key(pre+key, pre_node.children.get(key)))
            return word_list

        words = []
        # 情况一: 无前缀
        if not self.startswith(prefix):
            return words

        # 情况二: 若未前缀
        curNode = self.root
        for c in prefix:
            curNode = curNode.children.get(c)
        return _get_key(prefix, curNode)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('a')
    trie.insert('abandon')
    trie.insert('aad')
    trie.insert('aban')


    print(trie.search('a'))
    print(trie.search('ab'))
    print(trie.search('aban'))
    print(trie.search('aaddd'))

    print(trie.startswith('ab'))
    print(trie.startswith('aban'))
    print(trie.startswith('aaddd'))

    print(trie.findall('a'))


