from rockyutil.leetcode import *


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans = 0
        point = -1001
        for left, right in sorted(pairs, key = lambda x: x[1]):
            if point < left:
                point = right
                ans += 1
        return ans


sol = Solution()

eg_pairs = [[1, 2], [7, 8], [4, 5]]
print(sol.findLongestChain(pairs = eg_pairs))
