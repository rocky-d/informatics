from rockyutil.leetcode import *


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [''] * len(score)
        for (i, _), rank in zip(sorted(enumerate(score), key = lambda item: item[1], reverse = True), chain(('Gold Medal', 'Silver Medal', 'Bronze Medal'), map(str, range(4, len(score) + 1)))):
            ans[i] = rank
        return ans
