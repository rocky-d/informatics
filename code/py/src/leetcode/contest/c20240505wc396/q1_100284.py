class Solution:
    def isValid(self, word: str) -> bool:
        word_set = frozenset(word)
        return 3 <= len(word) and word.isalnum() and 0 < len(frozenset('aeiouAEIOU') & word_set) and 0 < len(
            frozenset('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ') & word_set)
