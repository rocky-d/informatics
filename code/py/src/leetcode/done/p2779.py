from rockyutil.leetcode import *


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        los = [num - k for num in nums]
        return max(bisect_right(los, hi) - idx for idx, hi in enumerate(num + k for num in nums))
