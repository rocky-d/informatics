from rockyutil.leetcode import *


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        ans = beans_sum = sum(beans)
        beans.sort()
        for times, bean in zip(range(len(beans), 0, -1), beans):
            ans = min(ans, beans_sum - times * bean)
        return ans


eg_beans = [3, 5, 6, 9]
print(Solution().minimumRemoval(beans = eg_beans))
