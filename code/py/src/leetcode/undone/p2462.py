from rockyutil.leetcode import *


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        heap_lft, heap_rit = [], []
        for lft, rit in zip(range(0, candidates, +1), range(-1, -1 - candidates, -1)):
            heappush(heap_lft, (costs[lft], lft)), heappush(heap_rit, (costs[rit], rit))
        seen = [False] * n
        lft, rit = candidates, -1 - candidates
        for _ in range(k):
            while seen[heap_lft[0][1]]:
                if lft < n:
                    heapreplace(heap_lft, (costs[lft], lft))
                    lft += 1
                else:
                    heappop(heap_lft)
            while seen[heap_rit[0][1]]:
                if -n <= rit:
                    heapreplace(heap_rit, (costs[rit], rit))
                    rit -= 1
                else:
                    heappop(heap_rit)
            if heap_lft[0][0] <= heap_rit[0][0]:
                if lft < n:
                    a, b = heapreplace(heap_lft, (costs[lft], lft))[0]
                    ans += a
                    seen[b] = True
                    lft += 1
                else:
                    a, b = heappop(heap_lft)[0]
                    ans += a
                    seen[b] = True
            else:
                if -n <= rit:
                    a, b = heapreplace(heap_rit, (costs[rit], rit))
                    ans += a
                    seen[b] = True
                    rit -= 1
                else:
                    a, b = heappop(heap_rit)[0]
                    ans += a
                    seen[b] = True
        return ans
