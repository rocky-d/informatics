from onlinejudge.leetcode import *


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnter = Counter()
        for num in nums1:
            num_isqrt = isqrt(num)
            for divisor in range(1, num_isqrt):
                if 0 == num % divisor:
                    cnter[divisor] += 1
                    cnter[num // divisor] += 1
            if 0 == num % num_isqrt:
                cnter[num_isqrt] += 1
                if num != num_isqrt * num_isqrt:
                    cnter[num // num_isqrt] += 1
        return sum(cnter[num * k] for num in nums2)
