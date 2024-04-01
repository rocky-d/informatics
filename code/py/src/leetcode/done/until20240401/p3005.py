from rockyutil.leetcode import *


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnter = Counter(Counter(nums).values())
        cnt = max(cnter.keys())
        return cnt * cnter[cnt]
