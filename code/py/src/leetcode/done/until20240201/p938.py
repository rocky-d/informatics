from rockyutil.leetcode import *


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val < low:
            res = self.rangeSumBST(root = root.right, low = low, high = high)
        elif high < root.val:
            res = self.rangeSumBST(root = root.left, low = low, high = high)
        else:
            res = root.val + self.rangeSumBST(root = root.left, low = low, high = high) + self.rangeSumBST(root = root.right, low = low, high = high)
        return res
