from rockyutil.leetcode import *


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else [root.val] + self.preorderTraversal(root = root.left) + self.preorderTraversal(root = root.right)
