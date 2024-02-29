from rockyutil.leetcode import *


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans = []
        dp = deque(((1, -1),), maxlen = len(nums))
        start = 1, 0
        nums.sort()
        for i in range(1, len(nums)):
            dp.append((1, -1))
            for j in range(i):
                if 0 == nums[i] % nums[j]:
                    if 1 + dp[j][0] > dp[-1][0]:
                        dp[-1] = 1 + dp[j][0], j
            if start[0] < dp[-1][0]:
                start = dp[-1][0], i
        index = start[1]
        while -1 != index:
            ans.append(nums[index])
            index = dp[index][1]
        return ans


eg_nums = [1, 2, 4, 8]
print(Solution().largestDivisibleSubset(eg_nums))
