from onlinejudge.leetcode import *


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        cnter = Counter(nums)
        for fr, to in zip(moveFrom, moveTo):
            cnter[to] += cnter.pop(fr)
        return sorted(cnter.keys())
