from leetcode.leetcode import *


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _j in range(1 + n)] for _i in range(1 + m)]
        for str_ in strs:
            zero_cnt = 0
            one_cnt = 0
            for ch in str_:
                if '0' == ch:
                    zero_cnt += 1
                else:  # elif '1' == ch:
                    one_cnt += 1
            for j1 in range(m, zero_cnt - 1, -1):
                for j2 in range(n, one_cnt - 1, -1):
                    dp[j1][j2] = max(dp[j1][j2], 1 + dp[j1 - zero_cnt][j2 - one_cnt])
        return dp[-1][-1]


sol = Solution()

eg_strs = ["10", "0001", "111001", "1", "0"]
eg_m = 5
eg_n = 3
print(sol.findMaxForm(strs = eg_strs, m = eg_m, n = eg_n))
