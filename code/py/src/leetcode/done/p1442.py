from rockyutil.leetcode import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefs = list(accumulate(arr, func = xor, initial = 0))
        return sum(k - i for i in range(n) for k in range(i + 1, n) if prefs[i] == prefs[k + 1])
