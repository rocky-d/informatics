from rockyutil.leetcode import *


class Trie:
    __slots__ = 'cnt', 'children'

    def __init__(self) -> None:
        self.cnt: int = 0
        self.children: Dict[str, Trie] = {}

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.cnt += 1

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                res = False
                break
            node = node.children[char]
        else:
            res = 0 < node.cnt
        return res

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.children:
                res = False
                break
            node = node.children[char]
        else:
            res = True
        return res
