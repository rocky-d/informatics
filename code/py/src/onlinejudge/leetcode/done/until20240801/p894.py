from onlinejudge.leetcode import *


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if 0b0 == 0b1 & n:
            return []
        dp = [[TreeNode(val = 0, left = None, right = None)]]
        for i in range(1, n // 2 + 1):
            dp.append([])
            for j, k in zip(range(0, i, +1), range(i - 1, -1, -1)):
                for lft in dp[j]:
                    for rit in dp[k]:
                        dp[-1].append(TreeNode(val = 0, left = lft, right = rit))
        return dp[-1]
