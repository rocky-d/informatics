from rockyutil.leetcode import *


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        dp = [0 for _ in range(n)]
        stack = []
        for i, x in enumerate(arr):
            while 0 < len(stack) and x < arr[stack[-1]]:
                stack.pop(-1)
            k = i - stack[-1] if 0 < len(stack) else 1 + i
            dp[i] = k * x + (dp[i - k] if 0 < len(stack) else 0)
            ans += dp[i]
            stack.append(i)
        return ans % 1_000_000_007


eg_arr = [3, 1, 2, 4]
print(Solution().sumSubarrayMins(arr = eg_arr))
