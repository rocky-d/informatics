from collections import deque
from typing import Optional, Tuple


def main() -> None:
    n, t, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = (map(int, input().split()) for _ in range(t))

    ans = deque(maxlen = t)
    a.insert(0, 0)

    class SegmentTreeNode(object):
        def __init__(self, segment: Tuple[int, int], val: int, lft: Optional['SegmentTreeNode'], rit: Optional['SegmentTreeNode']) -> None:
            self.segment = segment
            self.val = val
            self.lft = lft
            self.rit = rit

    def build(segment: Tuple[int, int]) -> SegmentTreeNode:
        if segment[0] == segment[1]:
            return SegmentTreeNode(val = a[segment[0]], lft = None, rit = None, segment = segment)
        mid = sum(segment) // 2
        lft, rit = build((segment[0], mid)), build((mid + 1, segment[1]))
        return SegmentTreeNode(val = max(lft.val, rit.val), lft = lft, rit = rit, segment = segment)

    root = build(segment = (1, n))

    def max_in(segment: Tuple[int, int], node: SegmentTreeNode) -> int:
        if segment == node.segment:
            return node.val
        mid = sum(node.segment) // 2
        if segment[1] <= mid:
            res = max_in(segment, node.lft)
        elif mid + 1 <= segment[0]:
            res = max_in(segment, node.rit)
        else:
            res = max(max_in((segment[0], mid), node.lft), max_in((mid + 1, segment[1]), node.rit))
        return res

    for l, r in queries:
        segment_max = max_in(segment = (l, r), node = root)
        ans.append(str(segment_max) + (' NO' if segment_max < q else ' YES'))
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
