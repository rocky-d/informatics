class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return 0 < sum(1 for char in s if char in 'aeiou')
