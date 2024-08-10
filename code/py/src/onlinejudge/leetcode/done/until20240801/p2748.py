from onlinejudge.leetcode import *


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(1 for i in range(n) for j in range(i + 1, n) if 1 == gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])))
