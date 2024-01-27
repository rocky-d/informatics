class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        pre = [0] + [1 for _ in range(1 + k)]
        for i in range(1, n):
            pre_last = pre
            pre = [0, 1]
            for j in range(1, 1 + k):
                pre.append(pre[-1] + pre_last[1 + j] - pre_last[max(0, j - i)])
        return (pre[-1] - pre[-2]) % 1_000_000_007


eg_n = 3
eg_k = 1
print(Solution().kInversePairs(n = eg_n, k = eg_k))
