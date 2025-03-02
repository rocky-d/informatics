from onlinejudge.leetcode import *


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans, depth_max = root.val, 0
        que = deque(((root, 0),))
        while 0 < len(que):
            node, depth = que.popleft()
            if depth_max < depth:
                ans, depth_max = node.val, depth
            if node.left is not None:
                que.append((node.left, depth + 1))
            if node.right is not None:
                que.append((node.right, depth + 1))
        return ans
