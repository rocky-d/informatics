from rockyutil.leetcode import *


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes, roots = {}, {}
        for parent, child, isleft in descriptions:
            if parent not in nodes.keys():
                nodes[parent] = TreeNode(val = parent)
                roots[parent] = True
            if child not in nodes.keys():
                nodes[child] = TreeNode(val = child)
            roots[child] = False
            if 1 == isleft:
                nodes[parent].left = nodes[child]
            else:  # elif 0 == isleft:
                nodes[parent].right = nodes[child]
        return [val for key, val in nodes.items() if True is roots[key]][0]
