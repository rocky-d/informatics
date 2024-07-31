from rockyutil.leetcode import *


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = str.maketrans('0123456789', ''.join(map(str, mapping)))
        return sorted(nums, key = lambda num: int(str(num).translate(mapping)))
