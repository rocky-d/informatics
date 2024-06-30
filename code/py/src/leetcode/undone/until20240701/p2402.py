from rockyutil.leetcode import *


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0] * n
        idle, using = list(range(n)), []
        meetings.sort(key = lambda m: m[0])
        for st, end in meetings:
            while using and using[0][0] <= st:
                heappush(idle, heappop(using)[1])  # 维护在 st 时刻空闲的会议室
            if len(idle) == 0:
                e, i = heappop(using)  # 没有可用的会议室，那么弹出一个最早结束的会议室（若有多个同时结束的，会弹出下标最小的）
                end += e - st  # 更新当前会议的结束时间
            else:
                i = heappop(idle)
            cnt[i] += 1
            heappush(using, (end, i))  # 使用一个会议室
        ans = 0
        for i, c in enumerate(cnt):
            if c > cnt[ans]:
                ans = i
        return ans
