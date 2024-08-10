from onlinejudge.leetcode import *


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> list[int]:
            if node is None:
                res = []
            else:
                left, right = dfs(node.left), dfs(node.right)
                res = [node.val] if len(left) == 0 and len(right) == 0 else left + right
            return res

        return dfs(root1) == dfs(root2)
