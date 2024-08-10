from onlinejudge.leetcode import *


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        line = tickets[k]
        for i in range(0, k + 1):
            ans += min(line, tickets[i])
        line -= 1
        for i in range(k + 1, len(tickets)):
            ans += min(line, tickets[i])
        return ans
