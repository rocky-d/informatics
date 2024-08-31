from onlinejudge.leetcode import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            total = maxHeights[i]
            last = maxHeights[i]
            for j in range(i - 1, -1, -1):
                if last < maxHeights[j]:
                    total += last
                else:
                    total += maxHeights[j]
                    last = maxHeights[j]
            last = maxHeights[i]
            for j in range(i + 1, n, +1):
                if last < maxHeights[j]:
                    total += last
                else:
                    total += maxHeights[j]
                    last = maxHeights[j]
            ans = max(ans, total)
        return ans


eg_maxHeights = [6, 5, 3, 9, 2, 7]
print(Solution().maximumSumOfHeights(maxHeights = eg_maxHeights))
