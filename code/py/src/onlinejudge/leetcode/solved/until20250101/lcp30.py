from onlinejudge.leetcode import *


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        ans = 0
        hp = 1
        heap_min = []
        nums_last = 0
        for num in nums:
            hp += num
            if num < 0:
                if 0 < hp:
                    heappush(heap_min, num)
                else:
                    ans += 1
                    val = heappushpop(heap_min, num)
                    hp -= val
                    nums_last += val
        return ans if 0 < hp + nums_last else -1


eg_nums = [100, 100, 100, -250, -60, -140, -50, -50, 100, 150]
print(Solution().magicTower(eg_nums))
