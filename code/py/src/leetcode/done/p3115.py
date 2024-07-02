from rockyutil.leetcode import *


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(num: int) -> bool:
            return 2 <= num and all(0 != num % divisor for divisor in range(2, isqrt(num) + 1))

        lft = 0
        while not is_prime(nums[lft]):
            lft += 1
        rit = len(nums) - 1
        while not is_prime(nums[rit]):
            rit -= 1
        return rit - lft
