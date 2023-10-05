class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        for _ in range(n - 2):
            first, second = second, first + second
        return 1 if n == 1 else second
