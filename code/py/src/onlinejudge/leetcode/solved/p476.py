class Solution:
    def findComplement(self, num: int) -> int:
        return ~num & (0b1 << num.bit_length() - 1) - 1
