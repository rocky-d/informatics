class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for _ in range(1, n):
            s = s + '1' + ''.join('0' if '1' == char else '1' for char in reversed(s))
        return s[k - 1]
