from onlinejudge.leetcode import *


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        ans = []
        que = deque()
        if root is not None:
            que.append((root, 0))
        while 0 < len(que):
            node, row = que.popleft()
            if row == len(ans):
                ans.append([])
            ans[-1].append(node.val)
            for child in node.children:
                if child is not None:
                    que.append((child, row + 1))
        return ans
