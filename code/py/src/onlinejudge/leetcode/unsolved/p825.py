from onlinejudge.leetcode import *


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0
        n = len(ages)
        ages.sort()
        idx = bisect_left(ages, 100)
        for x in range(idx):
            ans += (
                bisect_right(ages, ages[x]) - bisect_right(ages, 0.5 * ages[x] + 7) - 1
            )
        for x in range(idx, n):
            ans += (
                bisect_right(ages, ages[x]) - bisect_right(ages, 0.5 * ages[x] + 7) - 1
            )
        return ans


eg_ages = [16, 16]
print(Solution().numFriendRequests(eg_ages))
'''
ages[y] > 0.5 * ages[x] + 7
ages[y] <= ages[x]
ages[y] <= 100 | 100 <= ages[x] 
'''
