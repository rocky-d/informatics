from rockyutil.leetcode import *


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(0b1 == 0b1 & arr[i - 2] == 0b1 & arr[i - 1] == 0b1 & arr[i] for i in range(2, len(arr)))
