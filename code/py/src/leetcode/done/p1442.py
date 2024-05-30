from rockyutil.leetcode import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        prefs = list(accumulate(arr, func = xor, initial = 0))
        n = len(arr)
        for i in range(n):
            for k in range(i + 1, n):
                if prefs[i] == prefs[k + 1]:  # if prefs[i] ^ prefs[j] == prefs[j] ^ prefs[k + 1]:
                    ans += k - i
        return ans
