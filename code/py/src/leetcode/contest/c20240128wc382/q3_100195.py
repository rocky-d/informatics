class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m // 2) * ((n + 1) // 2) + (n // 2) * ((m + 1) // 2)


eg_n = 1
eg_m = 1
print(Solution().flowerGame(n = eg_n, m = eg_m))
