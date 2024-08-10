class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        tmp = limit + limit + 1
        return sum(i + 1 if i <= limit else max(0, tmp - i) for i in range(n - min(limit, n), n + 1))
