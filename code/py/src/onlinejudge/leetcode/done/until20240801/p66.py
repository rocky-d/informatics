from onlinejudge.leetcode import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(1 + int(''.join(map(str, digits))))]
