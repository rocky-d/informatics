from rockyutil.leetcode import *


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: Optional[TreeNode]) -> Union[bool, TreeNode]:
            if node is None:
                return False
            left, right = dfs(node = node.left), dfs(node = node.right)
            if isinstance(left, TreeNode):
                res = left
            elif isinstance(right, TreeNode):
                res = right
            elif left and right:
                res = node
            elif left or right:
                if p.val == node.val or q.val == node.val:
                    res = node
                else:
                    res = True
            else:
                if p.val == node.val or q.val == node.val:
                    res = True
                else:
                    res = False
            return res

        return dfs(node = root)
