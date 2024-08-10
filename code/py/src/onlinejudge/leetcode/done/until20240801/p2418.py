from onlinejudge.leetcode import *


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(heights)), key = lambda i: heights[i], reverse = True)]
