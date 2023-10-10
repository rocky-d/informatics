from leetcode.util import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        left, right = [], [triangle[0][0]]
        for i in range(1, len(triangle)):
            left, right = right, [triangle[i][0] + right[0]]
            for j in range(1, i):
                right.append(triangle[i][j] + min(left[j - 1], left[j]))
            right.append(triangle[i][-1] + left[-1])
        return min(right)


sol = Solution()

triangle_ls = [[-1], [3, 2], [-3, 1, -1]]
print(sol.minimumTotal(triangle_ls))
