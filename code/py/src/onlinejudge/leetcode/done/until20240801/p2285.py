from onlinejudge.leetcode import *


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnter = [0] * n
        for a, b in roads:
            cnter[a] += 1
            cnter[b] += 1
        return sum(cnt * num for num, cnt in enumerate(sorted(cnter), start = 1))
