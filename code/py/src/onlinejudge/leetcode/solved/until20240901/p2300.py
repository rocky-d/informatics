from onlinejudge.leetcode import *


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(map(neg, potions))
        return [bisect_right(range(len(potions)), -success, lo = 0, key = lambda mid: potions[mid] * spell) for spell in spells]
