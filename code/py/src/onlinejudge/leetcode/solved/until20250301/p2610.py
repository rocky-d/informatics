from onlinejudge.leetcode import *


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnter = sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)
        leng = len(cnter)
        i = 0
        for cnt in range(cnter[0][1], 0, -1):
            while i < leng and cnt == cnter[i][1]:
                i += 1
            ans.append([num for num, _ in cnter[:i]])
        return ans


eg_nums = [4, 5, 3, 3, 3]
print(Solution().findMatrix(eg_nums))
