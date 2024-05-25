from rockyutil.leetcode import *


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idxes = [idx for idx, num in enumerate(nums) if x == num]
        return [idxes[query - 1] if query <= len(idxes) else -1 for query in queries]
