from rockyutil.leetcode import *


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            res = []
        else:
            res = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return res
