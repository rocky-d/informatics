from onlinejudge.leetcode import *


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        que = deque()
        if root is not None:
            que.append((root, 0))
        while 0 < len(que):
            node, level = que.popleft()
            if level == len(ans):
                ans.insert(0, [])
            ans[0].append(node.val)
            if node.left is not None:
                que.append((node.left, level + 1))
            if node.right is not None:
                que.append((node.right, level + 1))
        return ans
