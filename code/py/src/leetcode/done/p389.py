class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in s:
            t = t.replace(char, '', 1)
        return t
