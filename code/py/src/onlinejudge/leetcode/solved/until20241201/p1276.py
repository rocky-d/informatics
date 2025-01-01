from onlinejudge.leetcode import *


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        return [] if tomatoSlices < 2 * cheeseSlices or 4 * cheeseSlices < tomatoSlices else (lambda x: [] if 0 != x % 2 else [x // 2, cheeseSlices - x // 2])(tomatoSlices - 2 * cheeseSlices)
