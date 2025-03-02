from onlinejudge.leetcode import *


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n_half = len(arr) >> 1
        cnt_ = 0
        for i, cnt in enumerate(sorted(Counter(arr).values(), reverse=True), start=1):
            cnt_ += cnt
            if n_half <= cnt_:
                ans = i
                break
        return ans
