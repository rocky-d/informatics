from rockyutil.leetcode import *


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        a, b = [], []
        for u, v in queries:
            idx1, idx2 = bisect_left(a, u), bisect_left(b, v)
            print(idx1, idx2)
            if idx1 == idx2:
                insort(a, u)
                insort(b, v)
            elif idx1 < idx2:
                for _ in range(idx1, idx2 + 1):
                    a.pop(idx1)
                    b.pop(idx1)
                insort(a, u)
                insort(b, v)
            print(a)
            print(b)
            ans.append(n - 1 - sum(bi - ai - 1 for ai, bi in zip(a, b)))
        return ans
