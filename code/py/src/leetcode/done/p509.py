class Solution:
    def fib(self, n: int) -> int:
        first, second = 0, 1
        for _ in range(n - 1):
            first, second = second, first + second
        return 0 if n == 0 else second
