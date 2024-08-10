from onlinejudge.leetcode import *


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        val_lst = 0
        que = deque(((root, 0),))
        while 0 < len(que):
            node, row = que.popleft()
            val = node.val
            if 0b0 == 0b1 & row and 0b1 == 0b1 & val and val_lst < val:
                val_lst = val if 0 < len(que) and row == que[0][1] else 1_000_001
            elif 0b1 == 0b1 & row and 0b0 == 0b1 & val and val < val_lst:
                val_lst = val if 0 < len(que) and row == que[0][1] else 0
            else:
                ans = False
                break
            if node.left is not None:
                que.append((node.left, row + 1))
            if node.right is not None:
                que.append((node.right, row + 1))
        else:
            ans = True
        return ans
