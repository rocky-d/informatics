from rockyutil.leetcode import *


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnter = Counter(accumulate((0b1 & num for num in nums), initial = 0))
        return sum(cnt * cnter[val - k] for val, cnt in cnter.items())
