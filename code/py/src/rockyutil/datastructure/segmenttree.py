from itertools import accumulate


class SegmentTreeNode(object):

    def __init__(self, lo, hi, val, lft, rit):
        self.lo = lo
        self.hi = hi
        self.val = val
        self.lft = lft
        self.rit = rit


def build(lo, hi):
    if lo == hi:
        return SegmentTreeNode(lo = lo, hi = hi, val = nums[lo], lft = None, rit = None)
    mid = lo + hi >> 1
    lft, rit = build(lo, mid), build(mid + 1, hi)
    return SegmentTreeNode(lo = lo, hi = hi, val = max(lft.val, rit.val), lft = lft, rit = rit)


def query(lo, hi, node):
    if node.lo == lo and node.hi == hi:
        return node.val
    mid = node.lo + node.hi >> 1
    if hi <= mid:
        res = query(lo, hi, node.lft)
    elif mid + 1 <= lo:
        res = query(lo, hi, node.rit)
    else:
        res = max(query(lo, mid, node.lft), query(mid + 1, hi, node.rit))
    return res


class SegmentTree(object):

    def __init__(self, func, vals, *, initial = None):
        self.func = func
        self.vals = vals
        self.initial = initial
        self.root = self._build(0, len(self.vals) - 1)
        del self.vals

    def _build(self, lo, hi):
        if lo == hi:
            return SegmentTreeNode(lo = lo, hi = hi, val = self.vals[lo] if self.initial is None else self.func(self.initial, self.vals[lo]), lft = None, rit = None)
        mid = lo + hi >> 1
        lft, rit = self._build(lo, mid), self._build(mid + 1, hi)
        return SegmentTreeNode(lo = lo, hi = hi, val = self.func(lft.val, rit.val), lft = lft, rit = rit)

    def _query(self, lo, hi, node):  # [lo, hi]
        if node.lo == lo and node.hi == hi:
            return node.val
        mid = node.lo + node.hi >> 1
        if hi <= mid:
            res = self._query(lo, hi, node.lft)
        elif mid + 1 <= lo:
            res = self._query(lo, hi, node.rit)
        else:
            res = self.func(self._query(lo, mid, node.lft), self._query(mid + 1, hi, node.rit))
        return res

    def query(self, lo, hi):  # [lo, hi)
        return self._query(lo, hi - 1, self.root)


if __name__ == '__main__':
    nums = [9, 1, 42, 5, 1, 6, 1, 45, 1, 4, 5, 6, 67, 78, 21, 1, 6, 1, 5]
    n = len(nums)

    root = build(lo = 0, hi = n - 1)
    print(query(lo = 3, hi = 6, node = root))

    root = SegmentTree(max, nums)
    print(root.query(lo = 3, hi = 7))
    accumulate()
