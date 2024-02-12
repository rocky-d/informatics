from rockyutil.leetcode import *


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else self.postorderTraversal(root = root.left) + self.postorderTraversal(root = root.right) + [root.val]
