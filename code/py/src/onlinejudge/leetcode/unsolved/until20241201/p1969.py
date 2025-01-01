class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        k = (0b1 << p) - 1
        return k * pow(k - 1, k >> 1, 1_000_000_007) % 1_000_000_007
