from rockyutil.leetcode import *


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        def dfs(node_a, node_b):
            nonlocal ans
            if node_a is None or node_b is None:
                return node_a is node_b
            if node_a.val == node_b.val:
                if dfs(node_a.left, node_b.left) and dfs(node_a.right, node_b.right):
                    if node_b is subRoot:
                        ans = True
                    return True
            dfs(node_a.left, node_b)
            dfs(node_a.right, node_b)
            return False

        dfs(node_a = root, node_b = subRoot)
        return ans
