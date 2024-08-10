from onlinejudge.leetcode import *


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        totals = []
        que = deque(((root, 0),))
        while 0 < len(que):
            node, row = que.popleft()
            if row == len(totals):
                totals.append(node.val)
            else:
                totals[-1] += node.val
            if node.left is not None:
                que.append((node.left, row + 1))
            if node.right is not None:
                que.append((node.right, row + 1))
        return -1 if len(totals) < k else nlargest(k, totals)[-1]
