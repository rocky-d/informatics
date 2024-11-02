from onlinejudge.leetcode import *


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) < k + candidates + candidates:
            return sum(sorted(costs)[:k])
        ans = 0
        heap_lft, heap_rit = costs[:candidates], costs[-candidates:]
        heapify(heap_lft), heapify(heap_rit)
        lft, rit = candidates, -candidates - 1
        for _ in range(k):
            if heap_lft[0] <= heap_rit[0]:
                ans += heapreplace(heap_lft, costs[lft])
                lft += 1
            else:
                ans += heapreplace(heap_rit, costs[rit])
                rit -= 1
        return ans
