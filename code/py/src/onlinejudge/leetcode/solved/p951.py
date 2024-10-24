from onlinejudge.leetcode import *


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is node2 is None:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            return (dfs(node1.left, node2.left) or dfs(node1.left, node2.right)) and (dfs(node1.right, node2.right) or dfs(node1.right, node2.left))

        return dfs(node1=root1, node2=root2)
