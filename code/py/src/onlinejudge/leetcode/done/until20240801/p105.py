from onlinejudge.leetcode import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idxes = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_lft: int, pre_rit: int, in_lft: int, in_rit: int) -> Optional[TreeNode]:
            if pre_rit < pre_lft or in_rit < in_lft:
                return None
            in_root = inorder_idxes[preorder[pre_lft]]
            return TreeNode(
                val = inorder[in_root],
                left = build(pre_lft = pre_lft + 1, pre_rit = pre_lft + (in_root - in_lft), in_lft = in_lft, in_rit = in_root - 1),
                right = build(pre_lft = pre_lft + (in_root - in_lft) + 1, pre_rit = pre_rit, in_lft = in_root + 1, in_rit = in_rit),
            )

        return build(pre_lft = 0, pre_rit = len(preorder) - 1, in_lft = 0, in_rit = len(inorder) - 1)
