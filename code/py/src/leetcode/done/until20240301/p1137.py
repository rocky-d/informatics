class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0, 1, 1
        for _ in range(n - 2):
            first, second, third = second, third, first + second + third
        return n if n < 2 else third
