from rockyutil.leetcode import *


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(1 + len(arr))]
        for i in range(1, 1 + len(arr)):
            max_ = 0
            for j in range(1, 1 + min(i, k)):
                max_ = max(max_, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + j * max_)
        return dp[-1]
