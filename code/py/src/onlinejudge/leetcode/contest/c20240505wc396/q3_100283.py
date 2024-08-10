from onlinejudge.leetcode import *


class Solution:
    def minAnagramLength(self, s: str) -> int:
        prefs = [[0] * 26]
        oft = ord('a')
        for char in s:
            cnt = prefs[-1].copy()
            cnt[ord(char) - oft] += 1
            prefs.append(cnt)

        def list_minus(a: List[int], b: List[int]) -> List[int]:
            res = []
            for ai, bi in zip(a, b):
                res.append(ai - bi)
            return res

        n = len(s)
        for factor in range(1, n):
            if 0 != n % factor:
                continue
            sample = list_minus(a = prefs[factor], b = prefs[0])
            for i in range(factor, n, factor):
                if sample != list_minus(a = prefs[i + factor], b = prefs[i]):
                    break
            else:
                ans = factor
                break
        else:
            ans = n
        return ans
