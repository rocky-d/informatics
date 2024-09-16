from onlinejudge.leetcode import *


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dct = {'a': 0b1, 'e': 0b10, 'i': 0b100, 'o': 0b1000, 'u': 0b10000}
        idxes = [[] for _ in range(32)]
        for idx, pref in enumerate(accumulate((dct.get(char, 0b0) for char in s), func=xor, initial=0)):
            idxes[pref].append(idx)
        return max((ls[-1] - ls[0] for ls in idxes if 2 <= len(ls)), default=0)
