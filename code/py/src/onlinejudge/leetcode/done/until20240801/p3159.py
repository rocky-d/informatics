from onlinejudge.leetcode import *


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idxes = [idx for idx, num in enumerate(nums) if x == num]
        return [-1 if len(idxes) < query else idxes[query - 1] for query in queries]
