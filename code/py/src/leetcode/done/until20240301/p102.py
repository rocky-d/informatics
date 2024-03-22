from rockyutil.leetcode import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        que = deque([(root, 0)])
        while 0 < len(que):
            node, level = que.popleft()
            if level == len(ans):
                ans.append([])
            ans[-1].append(node.val)
            if node.left is not None:
                que.append((node.left, level + 1))
            if node.right is not None:
                que.append((node.right, level + 1))
        return ans
