class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(char in 'aeiou' for char in s)
