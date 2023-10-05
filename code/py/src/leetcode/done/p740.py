from leetcode.util import *


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + num
        nums_order = sorted(nums_dict.keys())
        last_num = nums_order.pop(0)
        dp = [0, nums_dict[last_num]]
        for num in nums_order:
            dp.append(max(dp[-1], dp[-2] + nums_dict[num]) if last_num + 1 == num else dp[-1] + nums_dict[num])
            last_num = num
        return dp[-1]
