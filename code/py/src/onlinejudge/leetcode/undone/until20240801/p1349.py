from onlinejudge.leetcode import *


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[True, 0] for _ in range(n)]
        for i in range(m):
            new_dp = [[True, 0] for _ in range(n)]
            if '.' == seats[i][0] and dp[1][0]:
                new_dp[0] = [False, 1 + dp[0][1]]
            else:
                new_dp[0] = [True, dp[0][1]]
            for j in range(1, n - 1):
                if '.' == seats[i][j] and new_dp[j - 1][0] and dp[j - 1][0] and dp[j + 1][0]:
                    new_dp[j] = [False, 1 + max(dp[j][1], new_dp[j - 1][1])]
                else:
                    new_dp[j] = [True, max(dp[j][1], new_dp[j - 1][1])]
            else:
                if '.' == seats[i][-1] and new_dp[-2][0] and dp[-2][0]:
                    new_dp[-1] = [False, 1 + max(dp[-1][1], new_dp[-2][1])]
                else:
                    new_dp[-1] = [True, max(dp[-1][1], new_dp[-2][1])]
            print(new_dp)
            dp = new_dp
        return dp[-1][1]


eg_seats = [
    [".", "#"],
    ["#", "#"],
    ["#", "."],
    ["#", "#"],
    [".", "#"]
]
print(Solution().maxStudents(seats = eg_seats))
