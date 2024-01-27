class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] + [1 for _ in range(1 + k)]
        for i in range(1, n):
            dp_last = dp
            dp = [0, 1]
            for j in range(1, 1 + k):
                dp.append(dp[-1] + dp_last[1 + j] - dp_last[max(0, j - i)])
        return (dp[-1] - dp[-2]) % 1_000_000_007


eg_n = 3
eg_k = 1
print(Solution().kInversePairs(n = eg_n, k = eg_k))
