from onlinejudge.leetcode import *


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateSubtrees(start_val: int, stop_val: int) -> List[Optional[TreeNode]]:
            if start_val == stop_val:
                return [None]
            subtrees = []
            for root_node_val in range(start_val, stop_val):
                left_subtrees = generateSubtrees(start_val, root_node_val)
                right_subtrees = generateSubtrees(root_node_val + 1, stop_val)
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        subtrees.append(TreeNode(root_node_val, left_subtree, right_subtree))
            return subtrees

        return generateSubtrees(1, n + 1)
