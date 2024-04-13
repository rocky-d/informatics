from rockyutil.leetcode import *


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ins = [0 for _ in range(n)]
        for a, b in edges:
            ins[b] += 1
        winners = [i for i, val in enumerate(ins) if 0 == val]
        return winners[0] if 1 == len(winners) else -1
