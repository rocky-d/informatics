from rockyutil.leetcode import *


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (1 + maxChoosableInteger) // 2 < desiredTotal:
            return False

        @cache
        def dfs(nums: int, total: int) -> bool:
            for i in range(maxChoosableInteger):
                if 0b0 == 0b1 & (nums >> i):
                    if desiredTotal <= total + i + 1 or not dfs(nums = nums | (1 << i), total = total + i + 1):
                        res = True
                        break
            else:
                res = False
            return res

        return dfs(nums = 0, total = 0)


eg_maxChoosableInteger = 22
eg_desiredTotal = 242
print(Solution().canIWin(maxChoosableInteger = eg_maxChoosableInteger, desiredTotal = eg_desiredTotal))
