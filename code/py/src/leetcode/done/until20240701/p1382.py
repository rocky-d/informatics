from rockyutil.leetcode import *


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(node = root)

        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            return TreeNode(val = vals[mid], left = build(l, mid - 1), right = build(mid + 1, r))

        return build(l = 0, r = len(vals) - 1)
