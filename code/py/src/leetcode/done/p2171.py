from rockyutil.leetcode import *


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans_sum = sum(beans)
        return min(beans_sum - times * bean for times, bean in zip(range(len(beans), 0, -1), sorted(beans)))


eg_beans = [3, 5, 6, 9]
print(Solution().minimumRemoval(beans = eg_beans))
