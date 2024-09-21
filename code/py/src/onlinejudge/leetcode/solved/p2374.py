from onlinejudge.leetcode import *


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for u, v in enumerate(edges):
            scores[v] += u
        return max(range(len(edges)), key=lambda x: scores[x])
