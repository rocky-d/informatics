from onlinejudge.leetcode import *


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        bits_cnter = Counter()
        for num in nums:
            for i, bit in enumerate(bin(num)[:1:-1]):
                if '1' == bit:
                    bits_cnter[i] += 1
        for i, cnt in bits_cnter.items():
            if k <= cnt:
                ans |= 0b1 << i
        return ans


eg_nums = [7, 12, 9, 8, 9, 15]
eg_k = 4
print(Solution().findKOr(eg_nums, eg_k))
