from rockyutil.leetcode import *


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        people = 0b0
        head, n = 0, len(tickets)
        while True:
            ans += 1
            tickets[head] -= 1
            if 0 == tickets[head]:
                people |= 0b1 << head
                if k == head:
                    break
            head = (head + 1) % n
            while 0b1 == 0b1 & people >> head:
                head = (head + 1) % n
        return ans
