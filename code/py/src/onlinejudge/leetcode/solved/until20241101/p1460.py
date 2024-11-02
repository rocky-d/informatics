from onlinejudge.leetcode import *


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return all(x == y for x, y in zip(sorted(arr), sorted(target)))
