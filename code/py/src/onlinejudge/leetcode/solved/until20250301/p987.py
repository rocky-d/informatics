from onlinejudge.leetcode import *


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        grid = defaultdict(lambda: defaultdict(lambda: []))
        que = deque(((root, (0, 0)),))
        while 0 < len(que):
            node, (row, col) = que.popleft()
            insort(grid[col][row], node.val)
            if node.left is not None:
                que.append((node.left, (row + 1, col - 1)))
            if node.right is not None:
                que.append((node.right, (row + 1, col + 1)))
        return [reduce(lambda x, y: x + y, val.values()) for key, val in sorted(grid.items(), key = lambda item: item[0])]


eg_root = TreeNode(
    val = 1,
    left = TreeNode(
        val = 2,
        left = TreeNode(
            val = 4,
            left = None,
            right = None,
        ),
        right = TreeNode(
            val = 6,
            left = None,
            right = None,
        ),
    ),
    right = TreeNode(
        val = 3,
        left = TreeNode(
            val = 5,
            left = None,
            right = None,
        ),
        right = TreeNode(
            val = 7,
            left = None,
            right = None,
        ),
    ),
)
print(Solution().verticalTraversal(eg_root))
