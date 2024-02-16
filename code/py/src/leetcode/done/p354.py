from rockyutil.leetcode import *


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda envelope: (envelope[0], -envelope[1]))
        dp = [envelopes.pop(0)[1]]
        for _, ht in envelopes:
            if dp[-1] < ht:
                dp.append(ht)
            else:
                dp[bisect_left(dp, ht)] = ht
        return len(dp)


eg_envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(eg_envelopes))
