from onlinejudge.leetcode import *


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        ans = 0
        pairs = len(nums) * (len(nums) - 1) // 2
        words = list(map(str, nums))
        for i in range(len(words[0])):
            cnter = Counter()
            for word in words:
                cnter[word[i]] += 1
            ans += pairs - sum(val * (val - 1) // 2 for val in cnter.values())
        return ans


eg_nums = [13, 23, 12]
print(Solution().sumDigitDifferences(eg_nums))
