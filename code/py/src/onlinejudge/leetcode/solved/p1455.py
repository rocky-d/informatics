from onlinejudge.leetcode import *


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split(' '), start=1):
            if word.startswith(searchWord):
                ans = idx
                break
        else:
            ans = -1
        return ans
