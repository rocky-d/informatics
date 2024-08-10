from onlinejudge.leetcode import *


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        square_apples_list = [0]
        for frame_apples in (12 * i * i for i in range(1, 62997)):
            square_apples_list.append(square_apples_list[-1] + frame_apples)
        return 8 * bisect_left(square_apples_list, neededApples)


eg_neededApples = 1000000000
print(Solution().minimumPerimeter(neededApples = eg_neededApples))
