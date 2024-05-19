from rockyutil.leetcode import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        prefs = [0]
        for lst, nxt in pairwise(nums):
            if 0b1 & lst == 0b1 & nxt:
                prefs.append(prefs[-1] + 1)
            else:
                prefs.append(prefs[-1] + 0)
        for fr, to in queries:
            if 0 == prefs[to] - prefs[fr]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
