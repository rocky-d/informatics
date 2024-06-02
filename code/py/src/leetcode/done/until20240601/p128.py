from rockyutil.datastructure.unionfind import UnionFindList
from rockyutil.leetcode import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0
        nums = frozenset(nums)
        ufl = UnionFindList(len(nums), grouped = True)
        seen = dict()
        for i, num in enumerate(nums):
            if num - 1 in seen.keys():
                ufl.union(i, seen[num - 1])
            if num + 1 in seen.keys():
                ufl.union(i, seen[num + 1])
            seen[num] = i
        return len(max(ufl._groups.values(), key = lambda value: len(value)))
