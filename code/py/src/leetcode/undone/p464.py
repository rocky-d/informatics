from rockyutil.leetcode import *


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (1 + maxChoosableInteger) // 2 < desiredTotal:
            return False

        @cache
        def dfs(nums: int, remain: int) -> bool:
            for i in range(maxChoosableInteger):
                if 0b0 == 0b1 & (nums >> i):
                    if remain - i - 1 <= 0 or not dfs(nums = nums | (1 << i), remain = remain - i - 1):
                        res = True
                        break
            else:
                res = False
            return res

        return dfs(nums = 0, remain = desiredTotal)


eg_maxChoosableInteger = 22
eg_desiredTotal = 242
print(Solution().canIWin(maxChoosableInteger = eg_maxChoosableInteger, desiredTotal = eg_desiredTotal))
