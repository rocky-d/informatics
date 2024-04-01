from rockyutil.leetcode import *


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.prefs = list(accumulate(nums, initial = 0))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefs[right + 1] - self.prefs[left]
