from rockyutil.leetcode import *


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.removeLeafNodes(root.left, target), self.removeLeafNodes(root.right, target)
        if target == root.val and root.left is None and root.right is None:
            root = None
        return root
