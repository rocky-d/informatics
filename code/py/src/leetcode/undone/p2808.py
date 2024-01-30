from rockyutil.leetcode import *


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = floor((n - 1) / 2), ceil((n - 1) / 2)
        dists, nums_frozenset = {num: 0 for num in nums}, frozenset(nums)
        for i, num in enumerate(nums):
            dists_ = {num: n for num in nums}
            for j in range(1, 1 + left):
                index = i - j
                if num != nums[index]:
                    dists_[nums[index]] = min(dists_[nums[index]], j)
            for j in range(1, 1 + right):
                index = (i + j) % n
                if num != nums[index]:
                    dists_[nums[index]] = min(dists_[nums[index]], j)
            for num_ in nums_frozenset - frozenset((num,)):
                dists[num_] = max(dists[num_], dists_[num_])
        return min(dists.values())


eg_nums = [4, 8, 8, 13]
print(Solution().minimumSeconds(nums = eg_nums))
