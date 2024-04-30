from rockyutil.leetcode import *


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        ans = 0
        coins.sort()
        idx, n = 0, len(coins)
        cnt = 1
        while cnt <= target:
            if idx < n and coins[idx] <= cnt:
                cnt += coins[idx]
                idx += 1
            else:
                cnt <<= 1
                ans += 1
        return ans
