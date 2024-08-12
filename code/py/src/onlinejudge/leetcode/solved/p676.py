from onlinejudge.leetcode import *


class MagicDictionary:
    def __init__(self) -> None:
        self.dct = defaultdict(lambda: [])

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dct[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.dct[len(searchWord)]:
            if 1 == sum(1 for char1, char2 in zip(searchWord, word) if char1 != char2):
                res = True
                break
        else:
            res = False
        return res
