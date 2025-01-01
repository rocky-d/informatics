class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        chars = set(word)
        for char in chars:
            if char.islower() and char.upper() in chars:
                ans += 1
        return ans
