from collections import deque
from typing import Optional, Tuple


def main() -> None:
    n, t, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = (map(int, input().split()) for _ in range(t))

    ans = deque(maxlen = t)
    a.insert(0, 0)

    class SegmentTreeNode(object):
        def __init__(self, segment: Tuple[int, int], val: int, left: Optional['SegmentTreeNode'], right: Optional['SegmentTreeNode']) -> None:
            self.segment = segment
            self.val = val
            self.left = left
            self.right = right

    def build(lft: int, rit: int) -> SegmentTreeNode:
        if lft == rit:
            return SegmentTreeNode(val = a[lft], left = None, right = None, segment = (lft, rit))
        mid = (lft + rit) // 2
        left, right = build(lft, mid), build(mid + 1, rit)
        return SegmentTreeNode(val = max(left.val, right.val), left = left, right = right, segment = (lft, rit))

    root = build(lft = 1, rit = n)

    def max_in(segment: Tuple[int, int], node: SegmentTreeNode) -> int:
        if segment == node.segment:
            return node.val
        mid = sum(node.segment) // 2
        if segment[1] <= mid:
            res = max_in(segment, node.left)
        elif mid + 1 <= segment[0]:
            res = max_in(segment, node.right)
        else:
            res = max(max_in((segment[0], mid), node.left), max_in((mid + 1, segment[1]), node.right))
        return res

    for l, r in queries:
        segment_max = max_in(segment = (l, r), node = root)
        ans.append(str(segment_max) + (' NO' if segment_max < q else ' YES'))
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
