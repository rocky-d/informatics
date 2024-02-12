from rockyutil.leetcode import *


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = deque((nums[0],))
        dque_dec = deque((0,))
        for i in range(1, len(nums)):
            if dque_dec[0] < i - k:
                dque_dec.popleft()
            dp.append(dp[dque_dec[0]] + nums[i])
            while 0 < len(dque_dec) and dp[dque_dec[-1]] <= dp[-1]:
                dque_dec.pop()
            dque_dec.append(i)
        return dp[-1]


eg_nums = [10, -5, -2, 4, 0, 3]
eg_k = 3
print(Solution().maxResult(eg_nums, eg_k))
