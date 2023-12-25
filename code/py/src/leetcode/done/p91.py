class Solution:
    def numDecodings(self, s: str) -> int:
        if '0' == s[0]:
            ans = 0
        else:
            dp = 1, 1
            tens_digits = set(str(i) for i in range(10, 27))
            for i in range(1, len(s)):
                dp = dp[1], (dp[0] if s[i - 1:i + 1] in tens_digits else 0) + (dp[1] if s[i] != '0' else 0)
            ans = dp[-1]
        return ans


eg_s = '2101'
print(Solution().numDecodings(s = eg_s))
