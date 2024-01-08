from rockyutil.leetcode import *


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        node = root
        if node is None:
            res = 0
        elif node.val < low:
            res = self.rangeSumBST(node.right, low, high)
        elif high < node.val:
            res = self.rangeSumBST(node.left, low, high)
        else:
            res = node.val + self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)
        return res
