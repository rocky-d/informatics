from rockyutil.leetcode import *


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stk = deque([(-1, inf)])
        for _ in range(2):
            for idx, num in enumerate(nums):
                while stk[-1][1] < num:
                    ans[stk.pop()[0]] = num
                stk.append((idx, num))
        return ans
