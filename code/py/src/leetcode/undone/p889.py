from rockyutil.leetcode import *


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder_idxes, postorder_idxes = {val: idx for idx, val in enumerate(preorder)}, {val: idx for idx, val in enumerate(postorder)}

        def build(pre_lft: int, pre_rit: int, post_lft: int, post_rit: int) -> TreeNode:
            if pre_rit == pre_lft or post_rit == post_lft:
                return TreeNode(val = preorder[pre_lft])
            return TreeNode(
                val = preorder[pre_lft],
                left = build(pre_lft = pre_lft + 1, pre_rit = preorder_idxes[postorder[post_rit - 1]] - 1, post_lft = post_lft, post_rit = postorder_idxes[preorder[pre_lft + 1]]),
                right = build(pre_lft = preorder_idxes[postorder[post_rit - 1]], pre_rit = pre_rit, post_lft = postorder_idxes[preorder[pre_lft + 1]] + 1, post_rit = post_rit - 1),
            )

        return build(pre_lft = 0, pre_rit = len(preorder) - 1, post_lft = 0, post_rit = len(postorder) - 1)
