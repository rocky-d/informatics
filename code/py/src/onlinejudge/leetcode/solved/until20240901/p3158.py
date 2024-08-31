from onlinejudge.leetcode import *


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return reduce(xor, (num for num, cnt in Counter(nums).items() if 2 == cnt), 0)
