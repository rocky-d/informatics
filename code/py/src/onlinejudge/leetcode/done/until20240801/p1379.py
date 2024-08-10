from onlinejudge.leetcode import *


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        que = deque([(original, cloned)])
        while que[-1][0] is not target:
            node1, node2 = que.pop()
            if node1.left is not None:
                que.append((node1.left, node2.left))
            if node1.right is not None:
                que.append((node1.right, node2.right))
        return que[-1][1]
