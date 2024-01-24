from rockyutil.leetcode import *


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[int], Optional[int]]:
            if node is None:
                return 0, None
            nonlocal ans
            left, right = dfs(node.left), dfs(node.right)
            if left[1] is not None:
                ans = max(ans, right[0] + left[1])
                res = 1 + right[0], 1 + left[1]
            elif right[1] is not None:
                ans = max(ans, left[0] + right[1])
                res = 1 + left[0], 1 + right[1]
            elif start == node.val:
                ans = max(left[0], right[0])
                res = None, 1
            else:
                res = 1 + max(left[0], right[0]), None
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
                right = None,
            ),
            right = TreeNode(
                val = 2,
                left = None,
                right = None,
            ),
        ),
    ),
    right = TreeNode(
        val = 3,
        left = TreeNode(
            val = 10,
            left = None,
            right = None,
        ),
        right = TreeNode(
            val = 6,
            left = None,
            right = None,
        ),
    ),
)
eg_start = 3
print(Solution().amountOfTime(root = eg_root, start = eg_start))
