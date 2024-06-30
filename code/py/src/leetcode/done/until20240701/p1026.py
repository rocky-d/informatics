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
                mini_lft, maxi_lft = dfs(node.left)
                mini_rit, maxi_rit = dfs(node.right)
                mini, maxi = min(mini_lft, mini_rit), max(maxi_lft, maxi_rit)
                ans = max(ans, abs(mini - node.val), abs(maxi - node.val))
                res = min(mini, node.val), max(maxi, node.val)
            return res

        dfs(node = root)
        return ans
