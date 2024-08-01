from operator import add

from rockyutil.datastructure.linkednode import BinaryTreeNode


class SegmentTree(object):

    def __init__(self, __function, __iterable):
        self._func = __function
        self._vals = list(__iterable)
        self._n = len(self._vals)
        self._root = self._build(0, self._n - 1)
        del self._vals

    def _build(self, lft, rit):  # [lft, rit]
        if lft == rit:
            return BinaryTreeNode(val = self._vals[lft], lft = None, rit = None)
        mid0 = lft + rit >> 1
        mid1 = mid0 + 1
        lft, rit = self._build(lft, mid0), self._build(mid1, rit)
        return BinaryTreeNode(val = self._func(lft.val, rit.val), lft = lft, rit = rit)

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

    def update(self, lo, hi, key):  # [lo, hi)
        self._update(self._root, 0, self._n - 1, lo, hi, key)


def build(lft, rit):  # [lft, rit]
    if lft == rit:
        return BinaryTreeNode(val = nums[lft], lft = None, rit = None)
    mid0 = lft + rit >> 1
    mid1 = mid0 + 1
    lft, rit = build(lft, mid0), build(mid1, rit)
    return BinaryTreeNode(val = add(lft.val, rit.val), lft = lft, rit = rit)


def query(node, lft, rit, lo, hi):  # [lo, hi]
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


def update(node, lft, rit, lo, hi, key):  # [lo, hi]
    if lft == rit:
        node.val = key(node.val)
        return
    mid0 = lft + rit >> 1
    mid1 = mid0 + 1
    if hi <= mid0:
        update(node.lft, lft, mid0, lo, hi, key)
    elif mid1 <= lo:
        update(node.rit, mid1, rit, lo, hi, key)
    else:
        update(node.lft, lft, mid0, lo, mid0, key)
        update(node.rit, mid1, rit, mid1, hi, key)
    node.val = add(node.lft.val, node.rit.val)


if __name__ == '__main__':
    nums = [9, 1, 42, 5, 1, 6, 1, 45, 1, 4, 5, 6, 67, 78, 21, 1, 6, 1, 5]

    root = build(lft = 0, rit = len(nums) - 1)
    print(query(node = root, lft = 0, rit = len(nums) - 1, lo = 3, hi = 5))
    update(node = root, lft = 0, rit = len(nums) - 1, lo = 3, hi = 5, key = lambda val: val + 1000)
    print(query(node = root, lft = 0, rit = len(nums) - 1, lo = 3, hi = 5))

    root = SegmentTree(add, nums)
    print(root.query(lo = 3, hi = 6))
    root.update(lo = 3, hi = 6, key = lambda val: val + 1000)
    print(root.query(lo = 3, hi = 6))
