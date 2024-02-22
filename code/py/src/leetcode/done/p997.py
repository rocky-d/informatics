from rockyutil.leetcode import *


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts, trusted = {i: [] for i in range(1, 1 + n)}, {i: [] for i in range(1, 1 + n)}
        for a, b in trust:
            trusts[a].append(b), trusted[b].append(a)
        judges = tuple(i for i in range(1, 1 + n) if 0 == len(trusts[i]) and n - 1 == len(trusted[i]))
        return judges[0] if 1 == len(judges) else -1
