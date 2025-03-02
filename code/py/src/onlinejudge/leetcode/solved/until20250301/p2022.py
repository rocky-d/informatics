from onlinejudge.leetcode import *


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mn = m * n
        return [original[i : i + n] for i in range(0, mn, n)] if mn == len(original) else []
