from rockyutil.leetcode import *


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else self.inorderTraversal(root = root.left) + [root.val] + self.inorderTraversal(root = root.right)
