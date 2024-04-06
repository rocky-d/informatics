from rockyutil.leetcode import *


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        node = root
        while True:
            if node.val < lo:
                node = node.right
            elif hi < node.val:
                node = node.left
            else:
                break
        return node
