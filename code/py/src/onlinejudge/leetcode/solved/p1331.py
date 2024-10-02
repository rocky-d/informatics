from onlinejudge.leetcode import *


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        rank = 0
        lst = None
        for i, num in sorted(enumerate(arr), key=lambda item: item[1]):
            if lst != num:
                lst = num
                rank += 1
            ans[i] = rank
        return ans
