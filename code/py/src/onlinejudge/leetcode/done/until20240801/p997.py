from onlinejudge.leetcode import *


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = {i: 0 for i in range(1, 1 + n)}
        trusted = {i: 0 for i in range(1, 1 + n)}
        for a, b in trust:
            trusting[a] += 1
            trusted[b] += 1
        for i in range(1, 1 + n):
            if 0 == trusting[i] and n - 1 == trusted[i]:
                ans = i
                break
        else:
            ans = -1
        return ans
