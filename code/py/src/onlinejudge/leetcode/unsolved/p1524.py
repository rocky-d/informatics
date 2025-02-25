from onlinejudge.leetcode import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        prefs1 = list(accumulate((0b1 & num for num in arr), initial=0))
        prefs2 = list(accumulate((0b1 & num for num in prefs1), initial=0))
        print(arr)
        print([0b1 & num for num in arr])
        print(prefs1)
        print(prefs2)
        for i in range(len(arr)):
            print(i, prefs2[i + 1] if 0b0 == 0b1 & prefs1[i + 1] else i + 1 - prefs2[i + 1])
            ans += (prefs2[i + 1] if 0b0 == 0b1 & prefs1[i + 1] else i + 1 - prefs2[i + 1]) % 1_000_000_007
        return ans


eg_arr = [1, 3, 5]
print(Solution().numOfSubarrays(eg_arr))
#     1 4 5
#     1 0 1
#   0 1 1 2
# 0 0 1 2 2
