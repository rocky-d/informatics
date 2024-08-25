def main() -> None:
    n = int(input())
    arrays = (map(int, input().split(maxsplit=1)[1].split()) for _ in range(n))

    class SegmentTreeNode(object):

        def __init__(self, lazy, val, lft, rit, *, nod=None):
            self.lazy = lazy
            self.val = val
            self.lft = lft
            self.rit = rit
            self.nod = nod

    class SegmentTree1D(object):

        def __init__(self, __function, __iterable):
            self._func = __function
            self._vals = __iterable
            self._n = len(self._vals)
            self._root = self._build(0, self._n - 1)
            del self._vals

        def _pull(self, node):
            pass

        def _push(self, node):
            pass

        def _build(self, lft, rit):  # [lft, rit]
            if lft == rit:
                return SegmentTreeNode(
                    lazy=None, val=self._vals[lft], lft=None, rit=None
                )
            mid0 = lft + rit >> 1
            mid1 = mid0 + 1
            lft = self._build(lft, mid0)
            rit = self._build(mid1, rit)
            return SegmentTreeNode(
                lazy=None, val=self._func(lft.val, rit.val), lft=lft, rit=rit
            )

        def _query(self, node, lft, rit, lo, hi):  # [lo, hi]
            if lft == lo and hi == rit:  # lft <= lo <= hi <= rit
                return node.val
            mid0 = lft + rit >> 1
            mid1 = mid0 + 1
            if hi <= mid0:
                res = self._query(node.lft, lft, mid0, lo, hi)
            elif mid1 <= lo:
                res = self._query(node.rit, mid1, rit, lo, hi)
            else:
                res = self._func(
                    self._query(node.lft, lft, mid0, lo, mid0),
                    self._query(node.rit, mid1, rit, mid1, hi),
                )
            return res

        def query(self, lo, hi):  # [lo, hi)
            hi -= 1
            return self._query(self._root, 0, self._n - 1, lo, hi)

        def _update(self, node, lft, rit, lo, hi, key):  # [lo, hi]
            if lft == rit:
                node.val = key(node.val)
                return
            mid0 = lft + rit >> 1
            mid1 = mid0 + 1
            if hi <= mid0:
                self._update(node.lft, lft, mid0, lo, hi, key)
            elif mid1 <= lo:
                self._update(node.rit, mid1, rit, lo, hi, key)
            else:
                self._update(node.lft, lft, mid0, lo, mid0, key)
                self._update(node.rit, mid1, rit, mid1, hi, key)
            node.val = self._func(node.lft.val, node.rit.val)

        def update(self, lo, hi, *, key=None):  # [lo, hi)
            if key is None:
                return
            hi -= 1
            self._update(self._root, 0, self._n - 1, lo, hi, key)

    class SegmentTree2D(object):

        def __init__(self, __function, __iterable):
            self._func = __function
            self._vals = list(__iterable)
            self._n = len(self._vals)
            self._root = self._build(0, self._n - 1)
            del self._vals

        def _pull(self, node):
            pass

        def _push(self, node):
            pass

        def _build(self, lft, rit):  # [lft, rit]
            if lft == rit:
                nod = SegmentTree1D(min, self._vals[lft])
                return SegmentTreeNode(
                    lazy=None, val=nod._root.val, lft=None, rit=None, nod=nod
                )
            mid0 = lft + rit >> 1
            mid1 = mid0 + 1
            lft = self._build(lft, mid0)
            rit = self._build(mid1, rit)
            return SegmentTreeNode(
                lazy=None, val=self._func(lft.val, rit.val), lft=lft, rit=rit
            )

        def _query(self, node, lft, rit, lo, hi):  # [lo, hi]
            if lft == lo and hi == rit:  # lft <= lo <= hi <= rit
                return node.val
            mid0 = lft + rit >> 1
            mid1 = mid0 + 1
            if hi <= mid0:
                res = self._query(node.lft, lft, mid0, lo, hi)
            elif mid1 <= lo:
                res = self._query(node.rit, mid1, rit, lo, hi)
            else:
                res = self._func(
                    self._query(node.lft, lft, mid0, lo, mid0),
                    self._query(node.rit, mid1, rit, mid1, hi),
                )
            return res

        def query(self, lo, hi):  # [lo, hi)
            hi -= 1
            return self._query(self._root, 0, self._n - 1, lo, hi)

        def _update(self, node, lft, rit, lo, hi, key):  # [lo, hi]
            if lft == rit:
                node.nod.update(j - 1, j, key=lambda _: x)
                node.val = node.nod._root.val
                return
            mid0 = lft + rit >> 1
            mid1 = mid0 + 1
            if hi <= mid0:
                self._update(node.lft, lft, mid0, lo, hi, key)
            elif mid1 <= lo:
                self._update(node.rit, mid1, rit, lo, hi, key)
            else:
                self._update(node.lft, lft, mid0, lo, mid0, key)
                self._update(node.rit, mid1, rit, mid1, hi, key)
            node.val = self._func(node.lft.val, node.rit.val)

        def update(self, lo, hi, *, key=None):  # [lo, hi)
            # if key is None:
            #     return
            hi -= 1
            self._update(self._root, 0, self._n - 1, lo, hi, key)

    root = SegmentTree2D(min, map(list, arrays))

    ans = []
    q = int(input())
    for _ in range(q):
        typ, s = input().split(maxsplit=1)
        if '1' == typ:
            i, j, x = map(int, s.split())
            root.update(i - 1, i)
        else:  # elif '2' == typ:
            i = int(s)
            ans.append(root.query(0, i))
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
