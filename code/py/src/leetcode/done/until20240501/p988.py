from rockyutil.leetcode import *


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = chr(ord('z') + 1)
        oft = ord('a')

        def dfs(node: TreeNode, s: str) -> None:
            nonlocal ans
            s = chr(oft + node.val) + s
            if node.left is None and node.right is None:
                ans = min(ans, s)
            else:
                if node.left is not None:
                    dfs(node.left, s)
                if node.right is not None:
                    dfs(node.right, s)

        dfs(node = root, s = '')
        return ans
