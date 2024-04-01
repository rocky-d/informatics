from rockyutil.leetcode import *


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        min_pq_val, max_pq_val = min(p.val, q.val), max(p.val, q.val)
        while True:
            if root.val < min_pq_val:
                root = root.right
            elif max_pq_val < root.val:
                root = root.left
            else:
                break
        return root
