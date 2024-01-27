class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0 for _ in range(k)]
        pre = [0] + [1 for _ in range(1 + k)]
        for i in range(1, n):
            dp_last = dp
            dp = [1]
            pre_last = pre
            pre = [0, 1]
            for j in range(1, 1 + k):
                dp.append(pre_last[1 + j] - pre_last[max(0, j - i)])
                pre.append(pre[-1] + dp[-1])
        return dp[-1] % 1_000_000_007


eg_n = 3
eg_k = 1
print(Solution().kInversePairs(n = eg_n, k = eg_k))
