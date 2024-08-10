from onlinejudge.leetcode import *


class Solution:
    ans = -1000

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.ans
