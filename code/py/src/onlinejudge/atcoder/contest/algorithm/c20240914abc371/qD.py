from operator import add


class SegmentTreeNode(object):

    def __init__(self, val, lft, rit):
        self.val = val
        self.lft = lft
        self.rit = rit


class SegmentTree(object):

    def __init__(self, __function, __iterable):
        self._func = __function
        self._vals = list(__iterable)
        self._root = self._build(0, len(self._vals) - 1)
        del self._vals

    def _build(self, lft, rit):  # [lft, rit]
        if lft == rit:
            return SegmentTreeNode(
                val=(self._vals[lft][0], self._vals[lft][0], self._vals[lft][1]),
                lft=None,
                rit=None,
            )
        mid0 = lft + rit >> 1
        mid1 = mid0 + 1
        lft = self._build(lft, mid0)
        rit = self._build(mid1, rit)
        return SegmentTreeNode(
            val=(lft.val[0], rit.val[1], self._func(lft.val[-1], rit.val[-1])),
            lft=lft,
            rit=rit,
        )

    def _query(self, node, lo, hi):  # [lo, hi]
        if lo <= node.val[0] and node.val[1] <= hi:
            return node.val[-1]
        if node.lft is None:  # if node.rit is None:
            return 0
        if hi <= node.lft.val[1]:
            res = self._query(node.lft, lo, hi)
        elif node.rit.val[0] <= lo:
            res = self._query(node.rit, lo, hi)
        else:
            res = self._func(
                self._query(node.lft, lo, hi),
                self._query(node.rit, lo, hi),
            )
        return res

    def query(self, lo, hi):  # [lo, hi]
        return self._query(self._root, lo, hi)


def main() -> None:
    n = int(input())
    x = map(int, input().split())
    p = map(int, input().split())
    q = int(input())
    lr = (map(int, input().split()) for _ in range(q))

    ans = []
    root = SegmentTree(add, zip(x, p))
    for l, r in lr:
        ans.append(root.query(lo=l, hi=r))
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
