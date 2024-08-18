from onlinejudge.leetcode import *


class SegmentTreeNode(object):
    def __init__(self, val, lft, rit):
        self.val = val
        self.lft = lft
        self.rit = rit


class SegmentTree(object):
    def __init__(self, __iterable):
        self._vals = list(__iterable)
        self._n = len(self._vals)
        self._root = self._build(0, self._n - 1)
        del self._vals

    def _build(self, lft, rit):  # [lft, rit]
        if lft == rit:
            return SegmentTreeNode(val = 1, lft = None, rit = None)
        mid0 = lft + rit >> 1
        mid1 = mid0 + 1
        lft = self._build(lft, mid0)
        rit = self._build(mid1, rit)
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
        hi -= 1
        return self._query(self._root, 0, self._n - 1, lo, hi)


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        SegmentTree(s)
