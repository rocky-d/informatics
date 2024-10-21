from onlinejudge.leetcode import *


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        for cnt in range(len(s), 0, -1):
            for seps in combinations(range(1, len(s)), cnt - 1):
                lo = 0
                vis = set()
                for hi in chain(seps, [len(s)]):
                    part = s[lo:hi]
                    if part in vis:
                        break
                    vis.add(part)
                    lo = hi
                else:
                    ans = cnt
                    break
            else:
                continue
            break
        return ans
