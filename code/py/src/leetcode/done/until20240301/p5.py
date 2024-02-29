class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        len_ans = len(ans)
        lens = len(s)
        dp = [[True for __ in range(_ + 1)] + [False for __ in range(lens - _ - 1)] for _ in range(lens)]
        for right in range(lens):
            for left in range(right - 1, -1, -1):
                if dp[left + 1][right - 1] and s[left] == s[right]:
                    dp[left][right] = True
                    s_right = right + 1
                    if s_right - left > len_ans:
                        ans = s[left: s_right]
                        len_ans = len(ans)
        return ans


sol = Solution()

example_s = "babad"
print(sol.longestPalindrome(example_s))
