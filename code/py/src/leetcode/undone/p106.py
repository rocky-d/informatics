from rockyutil.leetcode import *


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idxes = {val: idx for idx, val in enumerate(inorder)}

        def func(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idxes[val]
            root.right = func(index + 1, in_right)
            root.left = func(in_left, index - 1)
            return root

        return func(0, len(inorder) - 1)
