from rockyutil.leetcode import *


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        ans = 0
        pairs = comb(len(nums))
        words = list(map(str, nums))
        for i in range(len(words[0])):
            cnter = Counter()
            for word in words:
                cnter[word[i]] += 1
            ans += pairs - sum(comb(val) for val in cnter.values())
        return ans
