from onlinejudge.leetcode import *


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefs = list(accumulate(arr, func=xor, initial=0b0))
        return [prefs[l] ^ prefs[r + 1] for l, r in queries]
