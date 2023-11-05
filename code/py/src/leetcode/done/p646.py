from rockyutil.leetcode import *


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[0])
        dp = []
        for i, pairs_i in enumerate(pairs):
            dp.append(1)
            for j, pairs_j in enumerate(pairs[:i]):
                if pairs_j[1] < pairs_i[0]:
                    dp[-1] = max(dp[-1], dp[j] + 1)
        return dp[-1]


sol = Solution()

eg_pairs = [[1, 2], [7, 8], [4, 5]]
sol.findLongestChain(pairs = eg_pairs)
