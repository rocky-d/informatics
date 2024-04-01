class Solution:
    def minInsertions(self, s: str) -> int:
        sb = s[::-1]
        dp1, dp2 = [0] + [0 for _ in sb], [0] + [0 for _ in sb]
        for s_i in s:
            for j, sb_j in enumerate(sb):
                dp2[j + 1] = dp1[j] + 1 if s_i == sb_j else max(dp1[j + 1], dp2[j])
            dp1, dp2 = dp2, dp1
        return len(s) - dp1[-1]


sol = Solution()

eg_s = "leetcode"
print(sol.minInsertions(s = eg_s))
