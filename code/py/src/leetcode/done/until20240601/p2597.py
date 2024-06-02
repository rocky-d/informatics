from rockyutil.leetcode import *


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        subsets = [[]]
        for num in nums:
            k1, k2 = num - k, num + k
            for i in range(len(subsets)):
                subset = subsets[i]
                if k1 not in subset and k2 not in subset:
                    subsets.append(subset + [num])
        return len(subsets) - 1
