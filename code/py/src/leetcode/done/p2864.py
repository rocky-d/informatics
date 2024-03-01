class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = s.count('0')
        return '1' * (len(s) - zeros - 1) + '0' * zeros + '1'
