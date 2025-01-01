from onlinejudge.leetcode import *


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        cnter = Counter(arr1)
        for num in arr2:
            ans += [num] * cnter.pop(num)
        for num in sorted(cnter.keys()):
            ans += [num] * cnter.pop(num)
        return ans
