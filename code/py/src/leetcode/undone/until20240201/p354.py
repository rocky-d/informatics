from rockyutil.leetcode import *


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda envelope: (envelope[0], -envelope[1]))
        dp = []
        for i, envelopes_i in enumerate(envelopes):
            dp.append(1)
            for j, envelopes_j in enumerate(envelopes[:i]):
                if envelopes_j[1] < envelopes_i[1]:
                    dp[-1] = max(dp[-1], dp[j] + 1)
        return max(dp)


sol = Solution()

eg_envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(sol.maxEnvelopes(envelopes = eg_envelopes))
