from rockyutil.leetcode import *


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda envelope: (envelope[0], -envelope[1]))
        dp = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            height = envelopes[i][1]
            if dp[-1] < height:  # if 0 == len(dp) or dp[-1] < height:
                dp.append(height)
            elif 1 == len(dp) or dp[-2] < height:
                dp[-1] = height
        return len(dp)


eg_envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(eg_envelopes))
