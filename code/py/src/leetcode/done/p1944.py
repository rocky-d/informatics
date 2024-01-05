from rockyutil.leetcode import *


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0 for _ in range(n)]
        decreasing_stack = [(0, heights[0])]
        for i in range(1, n):
            for j in range(len(decreasing_stack) - 1, -1, -1):
                ans[decreasing_stack[j][0]] += 1
                if decreasing_stack[j][1] < heights[i]:
                    decreasing_stack.pop(-1)
                else:
                    break
            decreasing_stack.append((i, heights[i]))
        return ans


eg_heights = [5, 1, 2, 3, 10]
print(Solution().canSeePersonsCount(heights = eg_heights))
