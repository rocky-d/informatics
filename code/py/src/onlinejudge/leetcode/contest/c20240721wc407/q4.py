from onlinejudge.leetcode import *


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ans = 0
        for negative, group in groupby((a - b for a, b in zip(nums, target)), key = lambda num: num < 0):
            stk = deque([0])
            for num in chain((map(neg, group) if negative else group), [0]):
                if num < stk[-1]:
                    ans += stk.pop() - num
                while num < stk[-1]:
                    stk.pop()
                stk.append(num)
        return ans


eg_nums = [1, 2, 3, 1, 1]
eg_target = [0, 0, 0, 0, 0]
print(Solution().minimumOperations(eg_nums, eg_target))
