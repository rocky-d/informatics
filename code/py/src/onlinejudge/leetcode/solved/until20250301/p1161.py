from onlinejudge.leetcode import *


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        que = deque([(root, 0)])
        while 0 < len(que):
            node, level = que.popleft()
            if level == len(levels):
                levels.append([])
            levels[-1].append(node.val)
            if node.left is not None:
                que.append((node.left, level + 1))
            if node.right is not None:
                que.append((node.right, level + 1))
        return 1 + max(enumerate(levels), key = lambda item: sum(item[1]))[0]
