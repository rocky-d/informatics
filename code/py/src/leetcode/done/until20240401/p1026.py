from rockyutil.leetcode import *


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: TreeNode) -> Tuple[int, int]:
            nonlocal ans
            if node.left is None and node.right is None:
                res = node.val, node.val
            elif node.left is not None and node.right is None:
                mini, maxi = dfs(node.left)
                ans = max(ans, abs(mini - node.val), abs(maxi - node.val))
                res = min(mini, node.val), max(maxi, node.val)
            elif node.left is None and node.right is not None:
                mini, maxi = dfs(node.right)
                ans = max(ans, abs(mini - node.val), abs(maxi - node.val))
                res = min(mini, node.val), max(maxi, node.val)
            else:  # elif node.left is not None and node.right is not None:
                left_min, left_max = dfs(node.left)
                right_min, right_max = dfs(node.right)
                mini, maxi = min(left_min, right_min), max(left_max, right_max)
                ans = max(ans, abs(mini - node.val), abs(maxi - node.val))
                res = min(mini, node.val), max(maxi, node.val)
            return res

        mini, maxi = dfs(node = root)
        ans = max(ans, abs(mini - root.val), abs(maxi - root.val))
        return ans
