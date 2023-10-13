class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for tail in range(1, len(s) + 1):
            head = max(0, tail - len(res) - 2)
            tmp = s[head:tail]
            if tmp == tmp[::-1]:
                res = tmp
            elif tmp[1:] == tmp[:0:-1]:
                res = tmp[1:]
        return res
