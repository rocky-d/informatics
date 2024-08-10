from onlinejudge.leetcode import *


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums_inc = []

        def dfs_inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs_inorder(node = node.left)
            nums_inc.append(node.val)
            dfs_inorder(node = node.right)

        dfs_inorder(node = root)
        nums_inc_1 = nums_inc + [-1]
        return [[query, query] if query == nums_inc_1[index] else [nums_inc_1[index - 1], nums_inc_1[index]] for query, index in zip(queries, map(lambda query: bisect_left(nums_inc, query), queries))]
