from rockyutil.leetcode import *


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)

        return max(dfs(root))
