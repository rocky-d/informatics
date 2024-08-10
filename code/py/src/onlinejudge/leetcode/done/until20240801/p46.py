from onlinejudge.leetcode import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(list(permutation) for permutation in permutations(nums))
