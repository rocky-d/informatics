from rockyutil.leetcode import *


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = deque([nums[0]])
        que = deque([0])
        for i in range(1, len(nums)):
            if que[0] < i - k:
                que.popleft()
            dp.append(dp[que[0]] + nums[i])
            while 0 < len(que) and dp[que[-1]] <= dp[-1]:
                que.pop()
            que.append(i)
        return dp[-1]


eg_nums = [10, -5, -2, 4, 0, 3]
eg_k = 3
print(Solution().maxResult(eg_nums, eg_k))
