from onlinejudge.leetcode import *


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        maxm = max(nums)
        primes = []
        tags = [False] * min(2, maxm) + [True] * max(0, maxm - 2)
        for num in range(2, maxm):
            if tags[num]:
                primes.append(num)
                for composite in range(num * num, maxm, num):
                    tags[composite] = False
        lst = 0
        for num in nums:
            if lst >= num:
                ans = False
                break
            idx = bisect_left(primes, num - lst)
            lst = num if 0 == idx else num - primes[idx - 1]
        else:
            ans = True
        return ans


eg_nums = [998, 2]
print(Solution().primeSubOperation(eg_nums))
