from rockyutil.leetcode import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        prefs = list(accumulate(arr, func = xor, initial = 0))
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if prefs[i] == prefs[k + 1]:  # prefs[i] ^ prefs[j] == prefs[j] ^ prefs[k + 1]
                        ans += 1
        return ans
