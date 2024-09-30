class Solution:
    def checkRecord(self, n: int) -> int:
        dp_p, dp_l1, dp_l2 = [1] + [0] * n, [0] + [0] * n, [0] + [0] * n
        for i in range(1, 1 + n):
            dp_p[i], dp_l1[i], dp_l2[i] = (dp_p[i - 1] + dp_l1[i - 1] + dp_l2[i - 1]) % 1_000_000_007, dp_p[i - 1], dp_l1[i - 1]
        return dp_p[-1] + dp_l1[-1] + dp_l2[-1]
