class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(frozenset(s))
