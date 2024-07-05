from typing import Tuple


def main() -> None:
    n, m, q = map(int, input().split())
    uvw = (tuple(map(int, input().split())) for _ in range(m))
    lr = (map(int, input().split()) for _ in range(q))

    ans = []
    heads = list(range(1 + n))

    def find(x: int) -> int:
        if x == heads[x]:
            return x
        heads[x] = find(heads[x])
        return heads[x]

    vals = [-1_000_000_001] * n
    groups = {x: 1 for x in range(1, 1 + n)}
    for u, v, w in sorted(uvw, key = lambda item: item[-1], reverse = True):
        u_head, v_head = find(u), find(v)
        if u_head != v_head:
            if groups[u_head] < groups[v_head]:
                heads[u] = heads[u_head] = v_head
                groups[v_head] += groups.pop(u_head)
            else:
                heads[v] = heads[v_head] = u_head
                groups[u_head] += groups.pop(v_head)
            vals[len(groups)] = w

    class SegmentTreeNode(object):
        def __init__(self, seg: Tuple[int, int], val: int, lft: 'SegmentTreeNode', rit: 'SegmentTreeNode') -> None:
            self.seg = seg
            self.val = val
            self.lft = lft
            self.rit = rit

    def build(l: int, r: int) -> SegmentTreeNode:
        if l == r:
            return SegmentTreeNode(seg = (l, r), val = vals[l], lft = None, rit = None)
        mid = l + r >> 1
        lft, rit = build(l, mid), build(mid + 1, r)
        return SegmentTreeNode(seg = (l, r), val = max(lft.val, rit.val), lft = lft, rit = rit)

    root = build(l = 1, r = n - 1)

    def query(l: int, r: int, node: SegmentTreeNode) -> int:
        if (l, r) == node.seg:
            return node.val
        mid = node.seg[0] + node.seg[1] >> 1
        if r <= mid:
            res = query(l, r, node.lft)
        elif mid + 1 <= l:
            res = query(l, r, node.rit)
        else:
            res = max(query(l, mid, node.lft), query(mid + 1, r, node.rit))
        return res

    for l, r in lr:
        res = query(l = l, r = r, node = root)
        ans.append('NO ANSWER' if -1_000_000_001 == res else res)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
