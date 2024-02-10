class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = n = len(s)
        dp = [True for _ in range(1 + n)], [True for _ in range(n)]
        for i in range(1, n):
            (dp_last0, _), dp = dp, (dp[1], [])
            for j in range(n - i):
                if dp_last0[j + 1] and s[j] == s[j + i]:
                    dp[1].append(True)
                    ans += 1
                else:
                    dp[1].append(False)
        return ans


eg_s = 'aaba'
print(Solution().countSubstrings(eg_s))
