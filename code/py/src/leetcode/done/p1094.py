from rockyutil.leetcode import *


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diffs = [capacity]
        for trip in trips:
            while len(diffs) <= trip[2]:
                diffs.append(0)
            diffs[trip[1]] -= trip[0]
            diffs[trip[2]] += trip[0]
        seats = 0
        for diff in diffs:
            seats += diff
            if seats < 0:
                ans = False
                break
        else:
            ans = True
        return ans


eg_trips = [[2, 1, 5], [3, 3, 7]]
eg_capacity = 5

print(Solution().carPooling(trips = eg_trips, capacity = eg_capacity))
