'''
@Time    : 2020/3/2 22:32
@FileName: 208trieNode.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 熟悉trie 如何插入之后，是一道常规题
# 参考文章
# https://juejin.im/post/5c2c096251882579717db3d2
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isWord = False
        self.word = ""


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            cVal = ord(c) - ord("a")
            if p.children[cVal]:
                p = p.children[cVal]
            else:
                newNode = TrieNode()
                p.children[cVal] = newNode
                p = newNode
        p.isWord = True
        p.word = word

    def helper(self, word):
        p = self.root
        for w in word:
            wCal = ord(w) - ord('a')
            if p.children[wCal]:
                p = p.children[wCal]
            else:
                return None
        return p

    def search(self, word):
        """a
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.helper(word)
        if p and p.isWord:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if self.helper(prefix):
            return True
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
