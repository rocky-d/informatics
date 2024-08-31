from onlinejudge.leetcode import *


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans
            if node is None:
                return depth
            depth += 1
            lft, rit = dfs(node = node.left, depth = depth), dfs(node = node.right, depth = depth)
            ans = max(ans, lft + rit - depth - depth)
            return max(lft, rit)

        dfs(node = root, depth = 0)
        return ans
