from rockyutil.leetcode import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = inf, inf
        for num in nums:
            if second < num:
                ans = True
                break
            elif first < num:
                second = num
            else:
                first = num
        else:
            ans = False
        return ans
