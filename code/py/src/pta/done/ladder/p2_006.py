from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, val: str, left: Optional['TreeNode'], right: Optional['TreeNode']) -> None:
        self.val = val
        self.left = left
        self.right = right


def main() -> None:
    n = int(input())
    postorder = input().split()
    inorder = input().split()

    ans = deque(maxlen = n)
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

    que = deque(((build(post_lft = 0, post_rit = n - 1, in_lft = 0, in_rit = n - 1), 0),))
    while 0 < len(que):
        node, row = que.popleft()
        ans.append(node.val)
        if node.left is not None:
            que.append((node.left, row + 1))
        if node.right is not None:
            que.append((node.right, row + 1))
    print(*ans)


if __name__ == '__main__':
    main()
