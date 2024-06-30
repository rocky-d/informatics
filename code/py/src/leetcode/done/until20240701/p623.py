from rockyutil.leetcode import *


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], dep: int) -> None:
            if node is None:
                return
            dep += 1
            if depth == dep:
                node.left = TreeNode(val = val, left = node.left, right = None)
                node.right = TreeNode(val = val, left = None, right = node.right)
            else:
                dfs(node.left, dep)
                dfs(node.right, dep)

        dummy = TreeNode(left = root, right = None)
        dfs(node = dummy, dep = 0)
        return dummy.left
