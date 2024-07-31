from rockyutil.leetcode import *


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        que = deque()
        if root is not None:
            que.append((root, 0))
        while 0 < len(que):
            node, level = que.popleft()
            if level == ans:
                ans += 1
            if node.left is not None:
                que.append((node.left, level + 1))
            if node.right is not None:
                que.append((node.right, level + 1))
        return ans
