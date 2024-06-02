from rockyutil.leetcode import *


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        n = len(plants)
        a, b = capacityA, capacityB
        for lft, rit in zip(range(0, n // 2, +1), range(n - 1, (n - 1) // 2, -1)):
            if a < plants[lft]:
                ans += 1
                a = capacityA
            if b < plants[rit]:
                ans += 1
                b = capacityB
            a -= plants[lft]
            b -= plants[rit]
        lft, rit = n // 2, (n - 1) // 2
        if lft == rit:
            if a < b:
                if b < plants[rit]:
                    ans += 1
                    b = capacityB
                b -= plants[rit]
            else:
                if a < plants[lft]:
                    ans += 1
                    a = capacityA
                a -= plants[lft]
        return ans
