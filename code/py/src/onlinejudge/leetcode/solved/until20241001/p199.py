from onlinejudge.leetcode import *


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        que = deque()
        if root is not None:
            que.append((root, 0))
        while 0 < len(que):
            node, row = que.popleft()
            if row == len(ans):
                ans.append(node.val)
            else:
                ans[-1] = node.val
            if node.left is not None:
                que.append((node.left, row + 1))
            if node.right is not None:
                que.append((node.right, row + 1))
        return ans
