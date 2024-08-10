from onlinejudge.leetcode import *


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        ones_idxes = [idx for idx, num in enumerate(nums) if 1 == num]
        print(ones_idxes)
        return ...


eg_nums = [1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
eg_k = 3
eg_maxChanges = 1
print(Solution().minimumMoves(eg_nums, eg_k, eg_maxChanges))
