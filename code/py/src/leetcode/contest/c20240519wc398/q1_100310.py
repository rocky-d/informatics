from rockyutil.leetcode import *


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for lst, nxt in pairwise(nums):
            if 0b1 & lst == 0b1 & nxt:
                ans = False
                break
        else:
            ans = True
        return ans
