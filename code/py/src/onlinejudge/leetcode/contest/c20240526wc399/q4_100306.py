from onlinejudge.leetcode import *


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = 0
        dp = [0, 0]
        for num in nums:
            dp.append(max(dp[-2] + num, dp[-1]))
        dp_len = len(dp)
        for pos, x in queries:
            if x == nums[pos]:
                ans += dp[-1]
                ans %= 1_000_000_007
                continue
            nums[pos] = x
            cnt = 1
            for i in range(pos + 2, dp_len):
                val = max(dp[i - 2] + nums[i - 2], dp[i - 1])
                if val == dp[i]:
                    cnt += 1
                    if 2 == cnt:
                        break
                else:
                    cnt = 0
                    dp[i] = val
            ans += dp[-1]
            ans %= 1_000_000_007
        return ans


nums = [3, 5, 9]
queries = [[1, -2], [0, -3]]
print(Solution().maximumSumSubsequence(nums, queries))
