from rockyutil.leetcode import *


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diffs = [capacity]
        for trip_passengers, trip_from, trip_to in trips:
            while len(diffs) <= trip_to:
                diffs.append(0)
            diffs[trip_from] -= trip_passengers
            diffs[trip_to] += trip_passengers
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
