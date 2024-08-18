from onlinejudge.leetcode import *


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        nums = sorted(((board[row][col], row, col) for row, col in product(range(m), range(n))), key = lambda item: item[0], reverse = True)
        hi = 3 * max(m, n)
        return max(nums[i][0] + nums[j][0] + nums[k][0]
                   for i in range(4)
                   for j in range(i + 1, hi) if nums[i][1] != nums[j][1] and nums[i][2] != nums[j][2]
                   for k in range(j + 1, hi) if nums[i][1] != nums[k][1] and nums[i][2] != nums[k][2] and nums[j][1] != nums[k][1] and nums[j][2] != nums[k][2])
