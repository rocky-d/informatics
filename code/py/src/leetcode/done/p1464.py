from rockyutil.leetcode import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (lambda list_: (list_[-1] - 1) * (list_[-2] - 1))(sorted(nums))
