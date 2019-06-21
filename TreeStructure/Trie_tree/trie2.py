"""
字典树（Trie): 使用纯字典实现
"""


class Trie(object):

    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        """
        insert a word into the trie
        :type word: str
        :rtype: void
        """
        curNode = self.root

        for c in word:
            if c not in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        curNode = self.root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]

        if self.end not in curNode:
                return False

        return True

    def startswith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for c in prefix:
            if c not in curNode:
                return False
            curNode = curNode[c]

        return True

    def findall(self, prefix):
        """
        Returns all words in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: list of suited words
        """
        def _get_key(pre, pre_node):
            word_list = []
            if pre_node.get(-1):
                word_list.append(pre)
            for key in pre_node.keys():
                if key != -1:
                    word_list.extend(_get_key(pre+key, pre_node.get(key)))
            return word_list

        words = []
        if not self.startswith(prefix):
            return words

        curNode = self.root
        for c in prefix:
            curNode = curNode.get(c)

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


