from onlinejudge.leetcode import *


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        maxm = -1
        for r in range(len(nums), 0, -1):
            for nums_sub in combinations(nums, r):
                res = reduce(or_, nums_sub)
                if maxm < res:
                    maxm = res
                    ans = 0
                if maxm == res:
                    ans += 1
        return ans
