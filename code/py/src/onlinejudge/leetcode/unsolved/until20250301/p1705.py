from onlinejudge.leetcode import *


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        n = len(apples)
        heap = []
        today = 0
        for apple, day in zip(apples, days):
            today += 1
            if 0 == apple == day:
                continue
            d, a = heappushpop(heap, (today + day, apple))
            while 0 < len(heap) and d <= today:
                d, a = heappop(heap)
            if 0 == len(heap):
                continue
            a -= 1
            ans += 1
            if 0 < a:
                heappush(heap, (d, a))
        while 0 < len(heap):
            today += 1
            d, a = heappop(heap)
            while 0 < len(heap) and d <= today:
                d, a = heappop(heap)
            if 0 == len(heap):
                break
            a -= 1
            ans += 1
            if 0 < a:
                heappush(heap, (d, a))
        return ans
