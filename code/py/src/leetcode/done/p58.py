class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        idx = len(s) - 1
        while ' ' == s[idx]:
            idx -= 1
        while 0 <= idx and ' ' != s[idx]:
            idx -= 1
            ans += 1
        return ans
