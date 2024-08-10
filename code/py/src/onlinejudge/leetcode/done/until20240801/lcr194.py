from onlinejudge.leetcode import *


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: Optional[TreeNode]) -> Union[bool, TreeNode]:
            if node is None:
                return False
            lft, rit = dfs(node.left), dfs(node.right)
            if isinstance(lft, TreeNode):
                res = lft
            elif isinstance(rit, TreeNode):
                res = rit
            elif lft and rit:
                res = node
            elif lft or rit:
                res = node if p.val == node.val or q.val == node.val else True
            else:
                res = True if p.val == node.val or q.val == node.val else False
            return res

        return dfs(node = root)
