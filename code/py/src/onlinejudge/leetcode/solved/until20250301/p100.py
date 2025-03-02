from onlinejudge.leetcode import *


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is None and q is None
        return p.val == q.val and self.isSameTree(p = p.left, q = q.left) and self.isSameTree(p = p.right, q = q.right)
