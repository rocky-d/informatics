from rockyutil.leetcode import *


class Solution:
    ans = -1000

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.ans = max(self.ans, node.val + left + right)
        return node.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans
