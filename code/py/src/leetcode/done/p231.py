class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 0 < n and 1 == bin(n).count('1')
