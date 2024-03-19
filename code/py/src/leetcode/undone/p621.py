from rockyutil.leetcode import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        val_max, val_max_cnt = max(Counter(Counter(tasks).values()).items(), key = lambda item: item[0])
        return max(len(tasks), val_max_cnt + (val_max - 1) * (n + 1))


eg_tasks = ['A', 'A', 'A', 'B', 'B', 'B']
eg_n = 2
print(Solution().leastInterval(eg_tasks, eg_n))
