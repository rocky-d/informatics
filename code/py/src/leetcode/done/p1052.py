from rockyutil.leetcode import *


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxm = cnt = sum(customers[i] for i in range(minutes) if 1 == grumpy[i])
        n = len(customers)
        for lft, rit in zip(range(0, n - minutes), range(minutes, n)):
            if 1 == grumpy[lft]:
                cnt -= customers[lft]
            if 1 == grumpy[rit]:
                cnt += customers[rit]
            maxm = max(maxm, cnt)
        return maxm + sum(c for c, g in zip(customers, grumpy) if 0 == g)
