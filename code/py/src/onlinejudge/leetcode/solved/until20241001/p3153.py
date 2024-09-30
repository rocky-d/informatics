from onlinejudge.leetcode import *


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        ans = comb(len(nums), 2) * len(str(nums[0]))
        words = list(map(str, nums))
        cnter = defaultdict(lambda: 0)
        for i in range(len(words[0])):
            cnter.clear()
            for word in words:
                cnter[word[i]] += 1
            ans -= sum(comb(val, 2) for val in cnter.values())
        return ans
