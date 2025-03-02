from onlinejudge.leetcode import *


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        obstacles = frozenset(map(tuple, obstacles))
        dirs, dirs_i = ((0, +1), (+1, 0), (0, -1), (-1, 0)), 0
        x, y = 0, 0
        for command in commands:
            if command < 0:
                if -1 == command:
                    dirs_i = (dirs_i + 1) % 4
                else:  # elif -2 == command:
                    dirs_i = (dirs_i - 1) % 4
            else:
                dx, dy = dirs[dirs_i]
                for _ in range(command):
                    vx, vy = x + dx, y + dy
                    if (vx, vy) in obstacles:
                        break
                    x, y = vx, vy
                ans = max(ans, x * x + y * y)
        return ans
