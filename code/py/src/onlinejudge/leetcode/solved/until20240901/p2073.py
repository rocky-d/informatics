from onlinejudge.leetcode import *


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x, y = tickets[k], tickets[k] - 1
        return sum(min(x, tickets[i]) for i in range(0, k + 1)) + sum(min(y, tickets[i]) for i in range(k + 1, len(tickets)))
