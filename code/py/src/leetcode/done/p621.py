from rockyutil.leetcode import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        heap1 = list((0, -val) for val in Counter(tasks).values())
        heapify(heap1)
        while 0 < len(heap1):
            heap2 = []
            while 0 < len(heap1) and heap1[0][0] <= ans:
                item = heappop(heap1)
                heappush(heap2, (item[1], item[0]))
            if 0 < len(heap2):
                item = heap2.pop(0)
                if 0 < -item[0] - 1:
                    heappush(heap1, (item[1] + n + 1, item[0] + 1))
                for item in heap2:
                    heappush(heap1, (item[1], item[0]))
            ans += 1
        return ans


eg_tasks = ['A', 'A', 'A', 'B', 'B', 'B']
eg_n = 2
print(Solution().leastInterval(eg_tasks, eg_n))
