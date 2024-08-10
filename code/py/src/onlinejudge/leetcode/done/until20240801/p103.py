from onlinejudge.leetcode import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        que = deque()
        if root is not None:
            que.append((root, 0, False))
        while 0 < len(que):
            node, row, reverse = que.popleft()
            if row == len(ans):
                ans.append([])
            if reverse:
                ans[-1].insert(0, node.val)
            else:
                ans[-1].append(node.val)
            if node.left is not None:
                que.append((node.left, row + 1, not reverse))
            if node.right is not None:
                que.append((node.right, row + 1, not reverse))
        return ans
