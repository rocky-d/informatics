from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, val: str, left: Optional['TreeNode'], right: Optional['TreeNode']) -> None:
        self.val = val
        self.left = left
        self.right = right


def main() -> None:
    n = int(input())
    inorder = input().split()
    preorder = input().split()

    ans = deque(maxlen = n)
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

    root = build(pre_lft = 0, pre_rit = n - 1, in_lft = 0, in_rit = n - 1)
    que = deque((root,))
    while 0 < len(que):
        node = que.popleft()
        ans.append(node.val)
        if node.right is not None:
            que.append(node.right)
        if node.left is not None:
            que.append(node.left)
    print(*ans)


if __name__ == '__main__':
    main()
