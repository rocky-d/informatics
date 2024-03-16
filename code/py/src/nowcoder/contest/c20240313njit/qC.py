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

    def build(l: int, r: int) -> SegmentTreeNode:
        if l == r:
            return SegmentTreeNode(segment = (l, r), val = a[l], lft = None, rit = None)
        mid = (l + r) // 2
        lft, rit = build(l, mid), build(mid + 1, r)
        return SegmentTreeNode(segment = (l, r), val = max(lft.val, rit.val), lft = lft, rit = rit)

    root = build(l = 1, r = n)

    def max_in(l: int, r: int, node: SegmentTreeNode) -> int:
        if (l, r) == node.segment:
            return node.val
        node_segment_mid = (node.segment[0] + node.segment[1]) // 2
        if r <= node_segment_mid:
            res = max_in(l, r, node.lft)
        elif node_segment_mid + 1 <= l:
            res = max_in(l, r, node.rit)
        else:
            res = max(max_in(l, node_segment_mid, node.lft), max_in(node_segment_mid + 1, r, node.rit))
        return res

    for l, r in queries:
        segment_max = max_in(l = l, r = r, node = root)
        ans.append(str(segment_max) + ' ' + ('NO' if segment_max < q else 'YES'))
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
