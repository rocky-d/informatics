from rockyutil.leetcode import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefs = list(accumulate(nums, initial = 0))
        prefs_idxes = {pref: i for i, pref in zip(range(len(prefs) - 1, -1, -1), reversed(prefs))}
        rit = 0
        for n in range(1 + prefs[-1] // k):
            nk = n * k
            while prefs[rit] < nk:
                rit += 1
            val = prefs[rit] - nk
            if val in prefs_idxes.keys() and 2 <= rit - prefs_idxes[val]:
                ans = True
                break
        else:
            ans = False
        return ans


eg_nums = [5, 0, 0, 0]
eg_k = 3
print(Solution().checkSubarraySum(eg_nums, eg_k))
