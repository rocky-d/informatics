from rockyutil.leetcode import *


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: TreeNode, num: int) -> None:
            nonlocal ans
            num = 10 * num + node.val
            if node.left is None and node.right is None:
                ans += num
            else:
                if node.left is not None:
                    dfs(node.left, num)
                if node.right is not None:
                    dfs(node.right, num)

        dfs(node = root, num = 0)
        return ans
