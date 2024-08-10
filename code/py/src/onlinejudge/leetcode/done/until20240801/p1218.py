from onlinejudge.leetcode import *


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(lambda: 0)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())


eg_arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
eg_difference = -2
print(Solution().longestSubsequence(eg_arr, eg_difference))
