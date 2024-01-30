from rockyutil.leetcode import *


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = floor((n - 1) / 2), ceil((n - 1) / 2)
        dists, nums_frozenset = {num: 0 for num in nums}, frozenset(nums)
        for i, num in enumerate(nums):
            dists_i = {num: n for num in nums}
            for j in range(1, 1 + left):
                index = i - j
                if num != nums[index]:
                    dists_i[nums[index]] = min(dists_i[nums[index]], j)
            for j in range(1, 1 + right):
                index = (i + j) % n
                if num != nums[index]:
                    dists_i[nums[index]] = min(dists_i[nums[index]], j)
            for target in nums_frozenset - frozenset((num,)):
                dists[target] = max(dists[target], dists_i[target])
        return min(dists.values())


eg_nums = [4, 8, 8, 13]
print(Solution().minimumSeconds(nums = eg_nums))
