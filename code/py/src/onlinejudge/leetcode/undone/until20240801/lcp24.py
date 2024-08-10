from onlinejudge.leetcode import *


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        ans = []
        lower, upper = [], []
        lower_sum, upper_sum = 0, 0
        for i in range(len(nums)):
            x = nums[i] - i
            if 0 == len(lower) or x <= -lower[0]:
                lower_sum += x
                heappush(lower, -x)
                if len(upper) + 1 < len(lower):
                    upper_sum -= lower[0]
                    heappush(upper, -lower[0])
                    lower_sum += heappop(lower)
            else:
                upper_sum += x
                heappush(upper, x)
                if len(lower) < len(upper):
                    lower_sum += upper[0]
                    heappush(lower, -upper[0])
                    upper_sum -= heappop(upper)
            ans.append((upper_sum - lower_sum if 0b1 == 0b1 & i else upper_sum - lower_sum - lower[0]) % 1_000_000_007)
        return ans
