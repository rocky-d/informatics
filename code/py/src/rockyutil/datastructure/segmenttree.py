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
        self._n = len(self._vals)
        self._root = self._build(0, self._n - 1)
        del self._vals

    def _build(self, lo, hi):
        if lo == hi:
            return SegmentTreeNode(val = self._vals[lo], lft = None, rit = None)
        mid = lo + hi >> 1
        lft, rit = self._build(lo, mid), self._build(mid + 1, hi)
        return SegmentTreeNode(val = self._func(lft.val, rit.val), lft = lft, rit = rit)

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
        return self._query(self._root, 0, self._n - 1, lo, hi - 1)


def build(lo, hi):
    if lo == hi:
        return SegmentTreeNode(val = nums[lo], lft = None, rit = None)
    mid = lo + hi >> 1
    lft, rit = build(lo, mid), build(mid + 1, hi)
    return SegmentTreeNode(val = add(lft.val, rit.val), lft = lft, rit = rit)


def query(node, lft, rit, lo, hi):
    if lft == lo and hi == rit:  # lft <= lo <= hi <= rit
        return node.val
    mid0 = lft + rit >> 1
    mid1 = mid0 + 1
    if hi <= mid0:
        res = query(node.lft, lft, mid0, lo, hi)
    elif mid1 <= lo:
        res = query(node.rit, mid1, rit, lo, hi)
    else:
        res = add(
            query(node.lft, lft, mid0, lo, mid0),
            query(node.rit, mid1, rit, mid1, hi),
        )
    return res


if __name__ == '__main__':
    nums = [9, 1, 42, 5, 1, 6, 1, 45, 1, 4, 5, 6, 67, 78, 21, 1, 6, 1, 5]

    root = build(lo = 0, hi = len(nums) - 1)
    print(query(node = root, lft = 0, rit = len(nums) - 1, lo = 3, hi = 5))

    root = SegmentTree(add, nums)
    print(root.query(lo = 3, hi = 6))
