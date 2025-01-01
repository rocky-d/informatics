from onlinejudge.leetcode import *


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        cnter = [0] * n
        for _, b in edges:
            cnter[b] += 1
        winners = [i for i, cnt in enumerate(cnter) if 0 == cnt]
        return winners[0] if 1 == len(winners) else -1
