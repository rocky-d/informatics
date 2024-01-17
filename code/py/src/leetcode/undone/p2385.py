from rockyutil.leetcode import *


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[int], Optional[int]]:
            if node is None:
                return 0, None
            nonlocal ans
            node_left, node_right = dfs(node.left), dfs(node.right)
            if node_left[1] is not None:
                res = 1 + node_right[0], 1 + node_left[1]
                ans = max(ans, res[0] + res[1])
            elif node_right[1] is not None:
                res = 1 + node_left[0], 1 + node_right[1]
                ans = max(ans, res[0] + res[1])
            elif start == node.val:
                res = None, -1
                ans = max(node_left[0], node_right[0])
            else:
                res = 1 + max(node_left[0], node_right[0]), None
            return res

        ans = 0
        dfs(root)
        return ans


eg_root = TreeNode(
    val = 1,
    left = TreeNode(
        val = 5,
        left = None,
        right = TreeNode(
            val = 4,
            left = TreeNode(
                val = 9,
                left = None,
                right = None
            ),
            right = TreeNode(
                val = 2,
                left = None,
                right = None
            )
        )
    ),
    right = TreeNode(
        val = 3,
        left = TreeNode(
            val = 10,
            left = None,
            right = None
        ),
        right = TreeNode(
            val = 6,
            left = None,
            right = None
        )
    )
)
eg_start = 3
print(Solution().amountOfTime(root = eg_root, start = eg_start))
