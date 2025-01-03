from onlinejudge.leetcode import *


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        ls = [(0, 1, 100_000_001)]
        for x_left, x_side in positions:
            for y_hight, y_left, y_side in reversed(ls):
                if x_left < y_left < x_left + x_side or y_left <= x_left < y_left + y_side:
                    insort(ls, (y_hight + x_side, x_left, x_side))
                    ans.append(ls[-1][0])
                    break
        return ans


eg_positions = [[1, 2], [2, 3], [6, 1]]
print(Solution().fallingSquares(eg_positions))
