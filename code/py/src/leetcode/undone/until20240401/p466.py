class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m, n = len(s1), len(s2)
        dp = []
        for i in range(n):
            left, right = i, 0
            for j in range(m):
                if s1[j] == s2[left]:
                    left += 1
                    if left == n:
                        left = 0
                        right += 1
            dp.append((left, right))
        ans = 0
        next_ = 0
        for _ in range(n1):
            ans += dp[next_][1]
            next_ = dp[next_][0]
        return ans // n2


eg_s1 = 'acb'
eg_n1 = 4
eg_s2 = 'ab'
eg_n2 = 2
print(Solution().getMaxRepetitions(s1 = eg_s1, n1 = eg_n1, s2 = eg_s2, n2 = eg_n2))
