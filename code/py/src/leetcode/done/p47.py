from rockyutil.leetcode import *


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(list(permutation) for permutation in frozenset(permutations(nums)))
