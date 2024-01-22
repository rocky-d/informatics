from rockyutil.leetcode import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeated_num = tuple(num for num, count in Counter(nums).items() if 2 == count)[0]
        return [repeated_num, repeated_num + n * (1 + n) // 2 - sum(nums)]


eg_nums = [1, 2, 2, 4]
print(Solution().findErrorNums(nums = eg_nums))
