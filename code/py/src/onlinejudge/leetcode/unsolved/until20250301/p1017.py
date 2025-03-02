class Solution:
    def baseNeg2(self, n: int) -> str:
        if 0 == n:
            return '0'
        ans = ''
        while 0 != n:
            remainder = 0b1 & n
            ans = str(remainder) + ans
            n = (n - remainder) // -2
        return ans
