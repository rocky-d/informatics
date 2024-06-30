from rockyutil.leetcode import *


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        dp = [0 for _ in range(len(arr))]
        stack = []
        for i, num in enumerate(arr):
            while 0 < len(stack) and num < arr[stack[-1]]:
                stack.pop(-1)
            k = i - stack[-1] if 0 < len(stack) else 1 + i
            dp[i] = k * num + (dp[i - k] if 0 < len(stack) else 0)
            ans += dp[i]
            stack.append(i)
        return ans % 1_000_000_007


eg_arr = [3, 1, 2, 4]
print(Solution().sumSubarrayMins(arr = eg_arr))
