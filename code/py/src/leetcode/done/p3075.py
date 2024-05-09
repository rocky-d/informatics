from rockyutil.leetcode import *


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(max(0, val - i) for i, val in enumerate(sorted(happiness, reverse = True)[:k]))
