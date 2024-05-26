from rockyutil.leetcode import *


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for num2 in nums2:
            divisor = num2 * k
            for num1 in nums1:
                if 0 == num1 % divisor:
                    ans += 1
        return ans
