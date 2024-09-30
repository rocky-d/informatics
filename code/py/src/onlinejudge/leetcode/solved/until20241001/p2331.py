from onlinejudge.leetcode import *


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if 0 == root.val:
            return False
        if 1 == root.val:
            return True
        if 2 == root.val:
            res = self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:  # elif 3 == root.val:
            res = self.evaluateTree(root.left) and self.evaluateTree(root.right)
        return res
