class Solution:
    def makeFancyString(self, s: str) -> str:
        ls = list(s)
        for i in range(len(ls) - 2):
            if ls[i] == ls[i + 1] == ls[i + 2]:
                ls[i] = ''
        return ''.join(ls)
