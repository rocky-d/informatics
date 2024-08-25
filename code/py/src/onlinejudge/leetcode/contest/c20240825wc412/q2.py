from onlinejudge.leetcode import *


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        for x, y in combinations(nums, r=2):
            if x == y:
                ans += 1
                continue
            x, y = str(x), str(y)
            if len(x) < len(y):
                x = '0' * (len(y) - len(x)) + x
            elif len(y) < len(x):
                y = '0' * (len(x) - len(y)) + y
            ls = [(xi, yi) for xi, yi in zip(x, y) if xi != yi]
            if 2 == len(ls) and ls[0][0] == ls[1][1] and ls[1][0] == ls[0][1]:
                ans += 1
        return ans
