from onlinejudge.leetcode import *


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans = 0
        for command in commands:
            char = command[0]
            if 'U' == char:
                ans -= n
            elif 'R' == char:
                ans += 1
            elif 'D' == char:
                ans += n
            else:  # elif 'L' == char:
                ans -= 1
        return ans
