class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if 0 == n else ~n & (0b1 << n.bit_length() - 1) - 1
