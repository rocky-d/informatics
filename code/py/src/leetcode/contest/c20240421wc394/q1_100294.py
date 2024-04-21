class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        chars = set(word)
        for s in chars:
            if s.islower() and s.upper() in chars:
                ans += 1
        return ans
