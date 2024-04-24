from rockyutil.leetcode import *


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[int], Optional[int]]:
            nonlocal ans
            if node is None:
                return 0, None
            lft, rit = dfs(node.left), dfs(node.right)
            if lft[1] is not None:
                ans = max(ans, rit[0] + lft[1])
                res = 1 + rit[0], 1 + lft[1]
            elif rit[1] is not None:
                ans = max(ans, lft[0] + rit[1])
                res = 1 + lft[0], 1 + rit[1]
            elif start == node.val:
                ans = max(lft[0], rit[0])
                res = None, 1
            else:
                res = 1 + max(lft[0], rit[0]), None
            return res

        dfs(node = root)
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
print(Solution().amountOfTime(eg_root, eg_start))
