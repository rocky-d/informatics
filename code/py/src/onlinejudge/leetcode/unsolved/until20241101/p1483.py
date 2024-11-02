from onlinejudge.leetcode import *


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]) -> None:
        m = n.bit_length() - 1
        ancestors = [[p] + [-1 for _ in range(m)] for p in parent]
        for i in range(m):
            for node in range(n):
                if -1 != ancestors[node][i]:
                    ancestors[node][i + 1] = ancestors[ancestors[node][i]][i]
        self.ancestors = ancestors

    def getKthAncestor(self, node: int, k: int) -> int:
        ancestors = self.ancestors
        for i in range(k.bit_length()):
            if 0b1 == 0b1 & k:
                node = ancestors[node][i]
                if -1 == node:
                    break
            k >>= 1
        return node
