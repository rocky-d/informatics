from rockyutil.leetcode import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        heap1 = list((0, -val) for val in Counter(tasks).values())
        heapify(heap1)
        while 0 < len(heap1):
            heap2 = []
            while 0 < len(heap1) and heap1[0][0] <= ans:
                cd, _val = heappop(heap1)
                heappush(heap2, (_val, cd))
            if 0 < len(heap2):
                _val, cd = heap2.pop(0)
                val = -_val - 1
                if 0 < val:
                    heappush(heap1, (cd + n + 1, -val))
                for _val, cd in heap2:
                    heappush(heap1, (cd, _val))
            ans += 1
        return ans


eg_tasks = ['A', 'A', 'A', 'B', 'B', 'B']
eg_n = 2
print(Solution().leastInterval(eg_tasks, eg_n))
