from onlinejudge.leetcode import *


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if node is None:
                return 0
            res = dfs(node.left) + dfs(node.right) + node.val - 1
            ans += abs(res)
            return res

        dfs(node = root)
        return ans
