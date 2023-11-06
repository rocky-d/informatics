from rockyutil.leetcode import *


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())


sol = Solution()

eg_arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
eg_difference = -2
print(sol.longestSubsequence(arr = eg_arr, difference = eg_difference))
