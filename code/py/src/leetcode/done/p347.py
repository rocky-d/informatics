from rockyutil.leetcode import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        return nlargest(n = k, iterable = frozenset(nums), key = lambda x: nums_counter[x])
