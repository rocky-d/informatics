from rockyutil.leetcode import *


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        lft, rit = 0, len(people) - 1
        while lft <= rit:
            if people[lft] + people[rit] <= limit:
                lft += 1
            rit -= 1
            ans += 1
        return ans
