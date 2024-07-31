from rockyutil.leetcode import *


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        a, b = 0, 2 * sum(possible) - len(possible)
        for i in range(len(possible) - 1):
            if 0 == possible[i]:
                a -= 1
                b += 1
            else:  # elif 1 == possible[i]:
                a += 1
                b -= 1
            if a > b:
                ans = i + 1
                break
        else:
            ans = -1
        return ans
