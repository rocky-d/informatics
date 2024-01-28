class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_odds, n_evens = (n + 1) // 2, n // 2
        m_odds, m_evens = (m + 1) // 2, m // 2
        return n_odds * m_evens + n_evens * m_odds


eg_n = 1
eg_m = 1
print(Solution().flowerGame(n = eg_n, m = eg_m))
