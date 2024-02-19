from rockyutil.leetcode import *


class Trie:
    __slots__ = 'cnt', 'children'

    def __init__(self) -> None:
        self.cnt: int = 0
        self.children: List[Optional[Trie]] = [None for _ in range(26)]

    def insert(self, word: str) -> None:
        node = self
        for index in map(lambda char: ord(char) - ord('a'), word):
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.cnt += 1

    def search(self, word: str) -> bool:
        node = self
        for index in map(lambda char: ord(char) - ord('a'), word):
            if node.children[index] is None:
                res = False
                break
            node = node.children[index]
        else:
            res = 0 < node.cnt
        return res

    def startsWith(self, prefix: str) -> bool:
        node = self
        for index in map(lambda char: ord(char) - ord('a'), prefix):
            if node.children[index] is None:
                res = False
                break
            node = node.children[index]
        else:
            res = True
        return res
