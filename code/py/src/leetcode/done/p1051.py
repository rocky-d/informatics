from rockyutil.leetcode import *


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for x, y in zip(heights, sorted(heights)) if x != y)
