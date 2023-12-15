from rockyutil.leetcode import *


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_node: Optional[TreeNode], right_node: Optional[TreeNode], is_odd_level: bool) -> None:
            if left_node is None or right_node is None:
                return
            if is_odd_level:
                left_node.val, right_node.val = right_node.val, left_node.val
            dfs(left_node.left, right_node.right, not is_odd_level)
            dfs(left_node.right, right_node.left, not is_odd_level)

        dfs(root.left, root.right, True)
        return root
