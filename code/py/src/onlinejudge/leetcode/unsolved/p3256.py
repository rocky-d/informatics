from onlinejudge.leetcode import *


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        ans = -3_000_000_000
        m, n = len(board), len(board[0])
        mn = m * n
        nums = sorted(((board[i][j], i, j) for i in range(m) for j in range(n)), key = lambda item: item[0],
                      reverse = True)
        for i in range(4):
            for j in range(i + 1, 3 * max(m, n)):
                for k in range(j + 1, 3 * max(m, n)):
                    if (nums[i][2] == nums[j][2] or nums[j][2] == nums[k][2] or nums[i][2] == nums[k][2] or
                            nums[i][1] == nums[j][1] or nums[j][1] == nums[k][1] or nums[i][1] == nums[k][1]):
                        continue
                    ans = max(ans, nums[i][0] + nums[j][0] + nums[k][0])
        return ans
