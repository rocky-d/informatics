from rockyutil.leetcode import *


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idxes = {val: idx for idx, val in enumerate(inorder)}

        def build(post_lft: int, post_rit: int, in_lft: int, in_rit: int) -> Optional[TreeNode]:
            if post_rit < post_lft or in_rit < in_lft:
                return None
            in_root = inorder_idxes[postorder[post_rit]]
            return TreeNode(
                val = inorder[in_root],
                left = build(post_lft = post_lft, post_rit = post_rit - (in_rit - in_root) - 1, in_lft = in_lft, in_rit = in_root - 1),
                right = build(post_lft = post_rit - (in_rit - in_root), post_rit = post_rit - 1, in_lft = in_root + 1, in_rit = in_rit),
            )

        return build(post_lft = 0, post_rit = len(postorder) - 1, in_lft = 0, in_rit = len(inorder) - 1)
