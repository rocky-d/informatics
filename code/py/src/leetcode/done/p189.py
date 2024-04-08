from rockyutil.leetcode import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop(-1))
