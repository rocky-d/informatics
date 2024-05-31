from rockyutil.leetcode import *


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        nums_xor_reduce = reduce(xor, nums)
        lowbit = nums_xor_reduce & -nums_xor_reduce
        for num in nums:
            ans[0 if 0b0 == num & lowbit else 1] ^= num
        return ans
