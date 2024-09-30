from onlinejudge.leetcode import *


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = sorted(60 * h + m for h, m in (map(int, hhmm.split(':')) for hhmm in timePoints))
        return min(1440 + nums[0] - nums[-1], min(nxt - lst for lst, nxt in pairwise(nums)))
