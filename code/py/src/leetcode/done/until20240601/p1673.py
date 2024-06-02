from rockyutil.leetcode import *


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stk = deque()
        n = len(nums)
        for i, num in enumerate(nums):
            while 0 < len(stk) and num < stk[-1] and k <= len(stk) + n - i - 1:
                stk.pop()
            stk.append(num)
        return list(stk)[:k]
