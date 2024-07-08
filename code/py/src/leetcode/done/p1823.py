from rockyutil.leetcode import *


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            ans = 1 + (ans - 1 + k) % i
        return ans
