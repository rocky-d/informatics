from rockyutil.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for times in Counter(nums).values():
            if 1 == times:
                ans = -1
                break
            else:  # elif 1 < times:
                ans += math.ceil(times / 3)
        return ans


eg_nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
print(Solution().minOperations(nums = eg_nums))
