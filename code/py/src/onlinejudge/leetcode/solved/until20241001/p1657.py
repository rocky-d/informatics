from onlinejudge.leetcode import *


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_counter, word2_counter = Counter(word1), Counter(word2)
        return word1_counter.keys() == word2_counter.keys() and sorted(word1_counter.values()) == sorted(word2_counter.values())
