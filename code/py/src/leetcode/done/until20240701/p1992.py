from rockyutil.leetcode import *


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(land), len(land[0])
        for r1, row in enumerate(land):
            for c1, val in enumerate(row):
                if 1 == val and (m == r1 + 1 or 0 == land[r1 + 1][c1]) and (n == c1 + 1 or 0 == row[c1 + 1]):
                    r2 = r1 - 1
                    while 0 <= r2 and 1 == land[r2][c1]:
                        r2 -= 1
                    c2 = c1 - 1
                    while 0 <= c2 and 1 == row[c2]:
                        c2 -= 1
                    ans.append([r2 + 1, c2 + 1, r1, c1])
        return ans
