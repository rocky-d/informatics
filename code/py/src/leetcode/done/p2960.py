from rockyutil.leetcode import *


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for val in batteryPercentages:
            if ans < val:
                ans += 1
        return ans
