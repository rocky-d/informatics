from rockyutil.leetcode import *


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if 0b0 == 0b1 & n:
            return []
        dp = deque([[], [TreeNode(val = 0, left = None, right = None)]])
        for nodes in range(3, 1 + n, 2):
            dp.append([]), dp.append([])
            for nodes_lft, nodes_rit in zip(range(1, nodes - 1, +2), range(nodes - 2, 0, -2)):
                for lft in dp[nodes_lft]:
                    for rit in dp[nodes_rit]:
                        dp[-1].append(TreeNode(val = 0, left = lft, right = rit))
        return dp[-1]
