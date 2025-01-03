class Solution:
    def isValid(self, word: str) -> bool:
        upps = frozenset(word.upper())
        return 3 <= len(word) and word.isalnum() and 1 <= len(upps & frozenset('AEIOU')) and 1 <= len(upps & frozenset('BCDFGHJKLMNPQRSTVWXYZ'))
