from rockyutil.leetcode import *


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        ans = n = len(nums)
        positions = defaultdict(lambda: [])
        for i, num in enumerate(nums):
            positions[num].append(i)
        for p in positions.values():
            res = n + p[0] - p[-1]
            for i in range(len(p)):
                res = max(res, p[i] - p[i - 1])
            ans = min(ans, res // 2)
        return ans


eg_nums = [4, 8, 8, 13]
print(Solution().minimumSeconds(nums = eg_nums))
