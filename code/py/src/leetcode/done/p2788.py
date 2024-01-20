from rockyutil.leetcode import *


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return sum([[w for w in word.split(separator) if 0 < len(w)] for word in words], [])
