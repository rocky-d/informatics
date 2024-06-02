from rockyutil.leetcode import *


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return (comb(n + 2, 2)
                - comb(3, 1) * comb(max(0, n + 2 - 1 * (limit + 1)), 2)
                + comb(3, 2) * comb(max(0, n + 2 - 2 * (limit + 1)), 2)
                - comb(3, 3) * comb(max(0, n + 2 - 3 * (limit + 1)), 2))
