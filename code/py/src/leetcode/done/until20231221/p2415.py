from rockyutil.leetcode import *


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_node: Optional[TreeNode], right_node: Optional[TreeNode], is_odd_level: bool) -> None:
            if left_node is None or right_node is None:
                return
            if is_odd_level:
                left_node.val, right_node.val = right_node.val, left_node.val
            dfs(left_node = left_node.left, right_node = right_node.right, is_odd_level = not is_odd_level)
            dfs(left_node = left_node.right, right_node = right_node.left, is_odd_level = not is_odd_level)

        dfs(left_node = root.left, right_node = root.right, is_odd_level = True)
        return root
