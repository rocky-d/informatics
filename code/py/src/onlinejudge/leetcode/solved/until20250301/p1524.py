from onlinejudge.leetcode import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        prefs1 = list(accumulate((0b1 & num for num in arr), initial=0))
        prefs2 = list(accumulate((0b1 & num for num in prefs1), initial=0))
        for i in range(1, 1 + len(arr)):
            ans += prefs2[i] if 0b0 == 0b1 & prefs1[i] else i - prefs2[i]
            ans %= 1_000_000_007
        return ans


eg_arr = [1, 3, 5]
print(Solution().numOfSubarrays(eg_arr))
