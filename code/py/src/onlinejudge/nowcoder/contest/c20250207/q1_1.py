from itertools import accumulate
from typing import List


class Solution:
    def maxlenEqualK(self, arr: List[int], k: int) -> int:
        prefs = list(accumulate(arr, initial=0))
        n = len(arr)

        def check(mid: int) -> bool:
            for lft, rit in zip(range(0, n + 1 - mid), range(mid, n + 1)):
                if k == prefs[rit] - prefs[lft]:
                    res = True
                    break
            else:
                res = False
            return res

        lo, hi = 0, n + 1
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if check(mid=mid):
                lo = mid
            else:
                hi = mid
        return lo


eg_arr = [0, 1, 2, 3]
eg_k = 3
print(Solution().maxlenEqualK(eg_arr, eg_k))
