from rockyutil.leetcode import *


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins_lcm = lcm(*coins)
        lcm_set = set()
        for coin in coins:
            for val in range(coin, coins_lcm + 1, coin):
                lcm_set.add(val)
        lcm_cnt = len(lcm_set)
        if k % lcm_cnt == 0:
            return (k // lcm_cnt) * coins_lcm
        lcm_times = k // lcm_cnt
        base_lcm = coins_lcm * lcm_times
        base_cnt = lcm_times * lcm_cnt
        lcm_set.clear()
        for coin in coins:
            for val in range(base_lcm + coin, base_lcm + coins_lcm + 1, coin):
                lcm_set.add(val)
        return sorted(lcm_set)[k - base_cnt - 1]


eg_coins = [5]
eg_k = 7
print(Solution().findKthSmallest(eg_coins, eg_k))
