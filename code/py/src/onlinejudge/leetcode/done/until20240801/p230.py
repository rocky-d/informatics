from onlinejudge.leetcode import *


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def dfs_inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs_inorder(node.left)
            inorder.append(node.val)
            dfs_inorder(node.right)

        dfs_inorder(node = root)
        return inorder[k - 1]
