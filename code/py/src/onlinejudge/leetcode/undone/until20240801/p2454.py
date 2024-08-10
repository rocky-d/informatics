from onlinejudge.leetcode import *


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        stack, heap = [], []
        for i in range(n):
            while 0 < len(heap) and heap[0][0] < nums[i]:
                ans[heapq.heappop(heap)[1]] = nums[i]
            while 0 < len(stack) and nums[stack[-1]] < nums[i]:
                pop = stack.pop(-1)
                heapq.heappush(heap, (nums[pop], pop))
            stack.append(i)
        return ans


eg_nums = [2, 4, 0, 9, 6]

print(Solution().secondGreaterElement(nums = eg_nums))
