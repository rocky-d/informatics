from rockyutil.leetcode import *


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        workers = sorted(worker)
        works = sorted(zip(difficulty, profit), key = lambda item: item[1], reverse = True)
        i, n = 0, len(works)
        while i < n and 0 < len(workers):
            idx = bisect_left(workers, works[i][0])
            if idx < len(workers):
                ans += works[i][1]
                workers.pop(idx)
            else:
                i += 1
        return ans
