from onlinejudge.leetcode import *


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k], tickets[i]) for i in range(0, k + 1)) + sum(min(tickets[k] - 1, tickets[i]) for i in range(k + 1, len(tickets)))
