from rockyutil.leetcode import *


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join((word[0] for word in words))
