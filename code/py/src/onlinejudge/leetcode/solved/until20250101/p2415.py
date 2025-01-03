from onlinejudge.leetcode import *


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(lft: Optional[TreeNode], rit: Optional[TreeNode], reverse: bool) -> None:
            if lft is None or rit is None:
                return
            if reverse:
                lft.val, rit.val = rit.val, lft.val
            reverse = not reverse
            dfs(lft.left, rit.right, reverse)
            dfs(lft.right, rit.left, reverse)

        dfs(lft=root.left, rit=root.right, reverse=True)
        return root
