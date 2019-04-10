"""
Implement a trie with insert, search, and startsWith methods.
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


import collections


class TrieNode:
    def __init__(self):
        # 设置字典的默认值(value)为TrieNode类型
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word):
        cur = self._root
        for e in word:
            cur = cur.children[e]
        cur.is_word = True

    def search(self, word):
        cur = self._root
        for e in word:
            cur = cur.children.get(e)
            if cur is None:
                return False
        return cur.is_word

    def starts_with(self, prefix):
        cur = self._root
        for e in prefix:
            cur = cur.children.get(e)
            if cur is None:
                return False
        return True
