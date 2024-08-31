from onlinejudge.leetcode import *


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
