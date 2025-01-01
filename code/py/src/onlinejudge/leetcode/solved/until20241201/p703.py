from onlinejudge.leetcode import *


class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]
