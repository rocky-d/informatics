from itertools import accumulate
from typing import List


class Solution:
    def maxlenEqualK(self, arr: List[int], k: int) -> int:
        prefs = list(accumulate(arr, initial=0))
        prefs_dct = {}
        for idx, pref in enumerate(prefs):
            if pref not in prefs_dct:
                prefs_dct[pref] = []
            prefs_dct[pref].append(idx)
        ans = 0
        for idx, pref in enumerate(prefs):
            target = pref - k
            if target in prefs_dct and prefs_dct[target][0] < idx:
                ans = max(ans, idx - prefs_dct[target][0])
        return ans


eg_arr = [0, 1, 2, 3]
eg_k = 3
print(Solution().maxlenEqualK(eg_arr, eg_k))
