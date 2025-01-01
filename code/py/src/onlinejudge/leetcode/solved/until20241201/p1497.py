from onlinejudge.leetcode import *


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnter = Counter(num % k for num in arr)
        return 0b0 == 0b1 & cnter[0] and (0b1 == 0b1 & k or 0b0 == 0b1 & cnter[k >> 1]) and all(cnter[i] == cnter[k - i] for i in range(1, k + 1 >> 1))
