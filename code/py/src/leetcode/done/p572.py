from rockyutil.leetcode import *


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def dfs(x: Optional[TreeNode], y: Optional[TreeNode]) -> bool:
            if x is None or y is None:
                return x is y
            return x.val == y.val and dfs(x.left, y.left) and dfs(x.right, y.right)

        return dfs(x = root, y = subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
