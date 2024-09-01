from onlinejudge.leetcode import *


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        def xorfunc(arr):
            if 1 == len(arr):
                return arr[0]
            return xorfunc([arr[i] ^ arr[i + 1] for i in range(len(arr) - 1)])

        @lru_cache(maxsize=None)
        def xorfuncij(i, j):
            return xorfunc(nums[i : j + 1])

        class SegmentTreeNode(object):

            def __init__(self, val, lft, rit):
                self.val = val
                self.lft = lft
                self.rit = rit

        class SegmentTree(object):

            def __init__(self):
                self._n = len(nums)
                self._root = self._build(0, self._n - 1)

            def _build(self, lft, rit):  # [lft, rit]
                if lft == rit:
                    return SegmentTreeNode(val=nums[lft], lft=None, rit=None)
                mid0 = lft + rit >> 1
                mid1 = mid0 + 1
                lftn = self._build(lft, mid0)
                ritn = self._build(mid1, rit)
                return SegmentTreeNode(
                    val=max(
                        lftn.val,
                        ritn.val,
                        max(
                            xorfuncij(i, j)
                            for i in range(lft, mid0 + 1)
                            for j in range(mid1, rit + 1)
                        ),
                    ),
                    lft=lftn,
                    rit=ritn,
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
                    res = max(
                        self._query(node.lft, lft, mid0, lo, mid0),
                        self._query(node.rit, mid1, rit, mid1, hi),
                        max(
                            xorfuncij(i, j)
                            for i in range(lft, mid0 + 1)
                            for j in range(mid1, rit + 1)
                        ),
                    )
                return res

            def query(self, lo, hi):  # [lo, hi]
                return self._query(self._root, 0, self._n - 1, lo, hi)

        root = SegmentTree()
        for lo, hi in queries:
            ans.append(root.query(lo, hi))
        return ans
