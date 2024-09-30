from onlinejudge.leetcode import *


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(1 for lo, hi in zip(startTime, endTime) if lo <= queryTime <= hi)
