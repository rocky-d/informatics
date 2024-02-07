class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        tags = [False for _ in range(2)] + [True for _ in range(2, n)]
        for num in range(2, n):
            if tags[num]:
                ans += 1
                for composite in range(num * num, n, num):
                    tags[composite] = False
        return ans


eg_n = 3
print(Solution().countPrimes(eg_n))
