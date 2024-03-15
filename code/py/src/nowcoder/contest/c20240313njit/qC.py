from collections import deque
from typing import Optional, Tuple


def main() -> None:
    n, t, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = (map(int, input().split()) for _ in range(t))

    ans = deque(maxlen = t)
    a.insert(0, 0)

    class TreeNode(object):
        def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode'], extent: Tuple[int, int]) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.extent = extent

    def build(lft: int, rit: int) -> TreeNode:
        if lft == rit:
            return TreeNode(val = a[lft], left = None, right = None, extent = (lft, rit))
        mid = (lft + rit) // 2
        left, right = build(lft, mid), build(mid + 1, rit)
        return TreeNode(val = max(left.val, right.val), left = left, right = right, extent = (lft, rit))

    root = build(lft = 1, rit = n)

    def max_in(extent: Tuple[int, int], node: TreeNode) -> int:
        if extent == node.extent:
            return node.val
        mid = sum(node.extent) // 2
        if extent[1] <= mid:
            res = max_in(extent, node.left)
        elif mid + 1 <= extent[0]:
            res = max_in(extent, node.right)
        else:
            res = max(max_in((extent[0], mid), node.left), max_in((mid + 1, extent[1]), node.right))
        return res

    for l, r in queries:
        lr_max = max_in(extent = (l, r), node = root)
        ans.append(str(lr_max) + (' NO' if lr_max < q else ' YES'))
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
