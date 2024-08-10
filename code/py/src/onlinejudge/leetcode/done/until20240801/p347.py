from onlinejudge.leetcode import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        return nlargest(k, frozenset(nums), key = lambda x: nums_counter[x])
