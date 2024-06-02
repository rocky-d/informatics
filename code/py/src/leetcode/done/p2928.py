from rockyutil.leetcode import *


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        n2, limit1 = n + 2, limit + 1
        return (comb(n2, 2)
                - comb(3, 1) * comb(max(0, n2 - 1 * limit1), 2)
                + comb(3, 2) * comb(max(0, n2 - 2 * limit1), 2)
                - comb(3, 3) * comb(max(0, n2 - 3 * limit1), 2))
