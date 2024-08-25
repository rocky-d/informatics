from onlinejudge.leetcode import *


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
