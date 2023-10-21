class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]]
        for ch1 in s1:
            dp.append([dp[-1][0] + ord(ch1)])
        for ch2 in s2:
            dp[0].append(dp[0][-1] + ord(ch2))
        for i, ch1 in enumerate(s1):
            i1 = i + 1
            for j, ch2 in enumerate(s2):
                dp[i1].append(dp[i][j] if ch1 == ch2 else min(dp[i1][j] + ord(ch2), dp[i][j + 1] + ord(ch1)))
        return dp[-1][-1]


sol = Solution()

eg_s1 = "delete"
eg_s2 = "leet"
print(sol.minimumDeleteSum(s1 = eg_s1, s2 = eg_s2))
