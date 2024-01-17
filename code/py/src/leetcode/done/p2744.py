from rockyutil.leetcode import *


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        words_set = set(words)
        for word in words:
            if word[::-1] in words_set and word[::-1] != word:
                res += 1
        return res // 2
