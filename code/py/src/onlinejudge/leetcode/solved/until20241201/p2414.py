class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 0
        i, n = 0, len(s)
        while i < n:
            leng = 1
            i += 1
            while i < n and ord(s[i - 1]) + 1 == ord(s[i]):
                leng += 1
                i += 1
            ans = max(ans, leng)
        return ans
