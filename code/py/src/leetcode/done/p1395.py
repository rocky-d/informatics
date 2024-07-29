from rockyutil.leetcode import *


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        n = len(rating)
        dp2 = [0] * n
        for lft in range(n):
            for rit in range(lft + 1, n):
                if rating[lft] < rating[rit]:
                    dp2[rit] += 1
        dp3 = [0] * n
        for lft in range(n):
            for rit in range(lft + 1, n):
                if rating[lft] < rating[rit]:
                    dp3[rit] += dp2[lft]
        ans += sum(dp3)
        dp2 = [0] * n
        for lft in range(n):
            for rit in range(lft + 1, n):
                if rating[lft] > rating[rit]:
                    dp2[rit] += 1
        dp3 = [0] * n
        for lft in range(n):
            for rit in range(lft + 1, n):
                if rating[lft] > rating[rit]:
                    dp3[rit] += dp2[lft]
        ans += sum(dp3)
        return ans


eg_rating = [2, 5, 3, 4, 1]
print(Solution().numTeams(eg_rating))
