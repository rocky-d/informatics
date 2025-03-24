from onlinejudge.leetcode import *


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        day = 1
        for lo, hi in sorted(meetings):
            ans += max(day, lo) - day
            day = max(day, hi + 1)
        ans += days - day + 1
        return ans


eg_days = 8
eg_meetings = [[3, 4], [4, 8], [2, 5], [3, 8]]
print(Solution().countDays(eg_days, eg_meetings))
