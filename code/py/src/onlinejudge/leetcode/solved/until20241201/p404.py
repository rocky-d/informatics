from onlinejudge.leetcode import *


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return (root.left.val if root.left is not None and root.left.left is None and root.left.right is None else self.sumOfLeftLeaves(root.left)) + self.sumOfLeftLeaves(root.right)
