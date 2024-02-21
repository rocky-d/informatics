from rockyutil.leetcode import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxes = {val: idx for idx, val in enumerate(inorder)}

        def func(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_right < preorder_left:
                return None
            preorder_root = preorder_left
            inorder_root = idxes[preorder[preorder_root]]
            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            root.left = func(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = func(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        return func(0, len(preorder) - 1, 0, len(preorder) - 1)
