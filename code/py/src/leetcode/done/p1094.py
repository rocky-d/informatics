from rockyutil.leetcode import *


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        states = []
        for trip in trips:
            while len(states) <= trip[2]:
                states.append(capacity)
            for i in range(trip[1], trip[2]):
                states[i] -= trip[0]
                if states[i] < 0:
                    return False
        return True
