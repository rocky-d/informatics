from onlinejudge.leetcode import *


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_times = sorted(Counter(nums).items(), key = lambda item: item[1], reverse = True)
        len_nums_times = len(nums_times)
        ans = []
        i = 0
        for times in range(nums_times[0][1], 0, -1):
            while i < len_nums_times and times == nums_times[i][1]:
                i += 1
            ans.append([num for num, times in nums_times[:i]])
        return ans


eg_nums = [4, 5, 3, 3, 3]
print(Solution().findMatrix(nums = eg_nums))
