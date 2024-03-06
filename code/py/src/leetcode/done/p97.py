class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[True] + [s2[:j] == s3[:j] for j in range(1, 1 + n)]] + [[s1[:i] == s3[:i]] for i in range(1, 1 + m)]
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                dp[i].append(dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


eg_s1 = 'aabcc'
eg_s2 = 'dbbca'
eg_s3 = 'aadbbcbcac'
print(Solution().isInterleave(eg_s1, eg_s2, eg_s3))
