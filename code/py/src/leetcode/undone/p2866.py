from rockyutil.leetcode import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left_stack, stack_sum, left_sums = [0], 0, []
        for i in range(0, n, +1):
            pop_times = 0
            while left_stack[-1] > maxHeights[i]:
                stack_sum -= left_stack.pop()
                pop_times += 1
            for _ in range(pop_times):
                left_stack.append(maxHeights[i])
            stack_sum += pop_times * left_stack[-1]
            left_sums.append(stack_sum)
            left_stack.append(maxHeights[i])
            stack_sum += left_stack[-1]
        right_stack, stack_sum, right_sums = [0], 0, []
        for i in range(n - 1, -1, -1):
            pop_times = 0
            while right_stack[-1] > maxHeights[i]:
                stack_sum -= right_stack.pop()
                pop_times += 1
            for _ in range(pop_times):
                right_stack.append(maxHeights[i])
            stack_sum += pop_times * right_stack[-1]
            right_sums.append(stack_sum)
            right_stack.append(maxHeights[i])
            stack_sum += right_stack[-1]
        ans = 0
        for i in range(n):
            ans = max(ans, left_sums[i] + maxHeights[i] + right_sums[-1 - i])
        return ans


eg_maxHeights = [6, 5, 3, 9, 2, 7]
print(Solution().maximumSumOfHeights(maxHeights = eg_maxHeights))
