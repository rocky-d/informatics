from onlinejudge.leetcode import *


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return sentence[0] == sentence[-1] and all(lst[-1] == nxt[0] for lst, nxt in pairwise(sentence.split(' ')))
