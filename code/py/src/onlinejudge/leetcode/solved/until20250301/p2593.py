from onlinejudge.leetcode import *


class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        tags = [False] * n
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapify(heap)
        while 0 < len(heap):
            num, idx = heappop(heap)
            if tags[idx]:
                continue
            ans += num
            for x in -1, 0, 1:
                x += idx
                if 0 <= x < n:
                    tags[x] = True
        return ans
