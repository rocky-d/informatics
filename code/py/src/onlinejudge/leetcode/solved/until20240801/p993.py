from onlinejudge.leetcode import *


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        targets = {x: None, y: None}

        def dfs(node: Optional[TreeNode], depth: int, parent: TreeNode) -> None:
            if node is None:
                return
            if node.val in targets:
                targets[node.val] = depth, parent.val
            depth += 1
            dfs(node.left, depth, node)
            dfs(node.right, depth, node)

        dfs(node=root, depth=0, parent=TreeNode(val=0, left=root, right=root))
        return targets[x][0] == targets[y][0] and targets[x][1] != targets[y][1]
