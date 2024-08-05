from rockyutil.leetcode import *


class Solution:
    def isSameTree(self, x: Optional[TreeNode], y: Optional[TreeNode]) -> bool:
        if x is None or y is None:
            return x is y
        return x.val == y.val and self.isSameTree(x.left, y.left) and self.isSameTree(x.right, y.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.isSameTree(x = root, y = subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
