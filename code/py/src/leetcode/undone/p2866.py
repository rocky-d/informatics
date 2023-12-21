from rockyutil.leetcode import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            sum_ = maxHeights[i]
            last = maxHeights[i]
            for j in range(i - 1, -1, -1):
                if last < maxHeights[j]:
                    sum_ += last
                else:
                    sum_ += maxHeights[j]
                    last = maxHeights[j]
            last = maxHeights[i]
            for j in range(i + 1, n, +1):
                if last < maxHeights[j]:
                    sum_ += last
                else:
                    sum_ += maxHeights[j]
                    last = maxHeights[j]
            ans = max(ans, sum_)
        return ans
