from rockyutil.leetcode import *


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> Tuple[int, int]:
            nonlocal ans
            if node.left is None and node.right is None:
                return node.val, node.val
            elif node.left is not None and node.right is None:
                min_, max_ = dfs(node.left)
                ans = max(ans, abs(min_ - node.val), abs(max_ - node.val))
                return min(min_, node.val), max(max_, node.val)
            elif node.left is None and node.right is not None:
                min_, max_ = dfs(node.right)
                ans = max(ans, abs(min_ - node.val), abs(max_ - node.val))
                return min(min_, node.val), max(max_, node.val)
            else:
                left_min, left_max = dfs(node.left)
                right_min, right_max = dfs(node.right)
                min_, max_ = min(left_min, right_min), max(left_max, right_max)
                ans = max(ans, abs(min_ - node.val), abs(max_ - node.val))
                return min(min_, node.val), max(max_, node.val)

        ans = 0
        min_, max_ = dfs(root)
        ans = max(ans, abs(min_ - root.val), abs(max_ - root.val))
        return ans
