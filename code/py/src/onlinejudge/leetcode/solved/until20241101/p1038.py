from onlinejudge.leetcode import *


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal val
            if node is None:
                return 0
            dfs(node.right)
            node.val += val
            val = node.val
            dfs(node.left)
            return node.val

        dfs(node = root)
        return root
