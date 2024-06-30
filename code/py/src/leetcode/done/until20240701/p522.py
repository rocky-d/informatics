from rockyutil.leetcode import *


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(x: str, y: str) -> bool:
            m, n = len(x), len(y)
            if m < n:
                return True
            if m == n:
                return x != y
            j = 0
            for xi in x:
                if xi == y[j]:
                    j += 1
                    if j == n:
                        res = False
                        break
            else:
                res = True
            return res

        strs.sort(key = len, reverse = True)
        for i, si in enumerate(strs):
            if all(i == j or check(x = sj, y = si) for j, sj in enumerate(strs)):
                ans = len(si)
                break
        else:
            ans = -1
        return ans
