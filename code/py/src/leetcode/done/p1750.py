class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        lft, rit = 0, n - 1
        while lft < rit and s[lft] == s[rit]:
            char = s[lft]
            while lft < n and char == s[lft]:
                lft += 1
            while 0 <= rit and char == s[rit]:
                rit -= 1
        return max(0, rit - lft + 1)
