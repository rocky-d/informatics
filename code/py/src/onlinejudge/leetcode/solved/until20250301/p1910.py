class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ls = s.split(sep=part, maxsplit=1)
        while 2 == len(ls):
            ls = ''.join(ls).split(sep=part, maxsplit=1)
        return ls[0]
