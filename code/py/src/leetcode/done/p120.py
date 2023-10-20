from rockyutil.leetcode import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        first, second = [], [triangle[0][0]]
        for i in range(1, len(triangle)):
            first, second = second, [triangle[i][0] + second[0]]
            for j in range(1, i):
                second.append(triangle[i][j] + min(first[j - 1], first[j]))
            second.append(triangle[i][-1] + first[-1])
        return min(second)


sol = Solution()

example_triangle = [[-1], [3, 2], [-3, 1, -1]]
print(sol.minimumTotal(example_triangle))
