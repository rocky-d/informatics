from rockyutil.leetcode import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        pre, suf = [0 for _ in range(n)], [0 for _ in range(n)]
        stack1, stack2 = [], []
        for i in range(0, n, +1):
            while 0 < len(stack1) and maxHeights[i] < maxHeights[stack1[-1]]:
                stack1.pop()
            pre[i] = (1 + i) * maxHeights[i] if 0 == len(stack1) else pre[stack1[-1]] + (i - stack1[-1]) * maxHeights[i]
            stack1.append(i)
        for i in range(n - 1, -1, -1):
            while 0 < len(stack2) and maxHeights[i] < maxHeights[stack2[-1]]:
                stack2.pop()
            suf[i] = (n - i) * maxHeights[i] if 0 == len(stack2) else suf[stack2[-1]] + (stack2[-1] - i) * maxHeights[i]
            stack2.append(i)
            ans = max(ans, pre[i] + suf[i] - maxHeights[i])
        return ans


eg_maxHeights = [6, 5, 3, 9, 2, 7]
print(Solution().maximumSumOfHeights(maxHeights = eg_maxHeights))
