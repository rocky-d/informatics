class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk, ls = [], []
        for i, char in enumerate(s):
            if '(' == char:
                stk.append(i)
            elif ')' == char:
                if 0 < len(stk):
                    stk.pop()
                else:
                    ls.append(i)
        for i in sorted(stk + ls, reverse = True):
            s = s[:i] + s[i + 1:]
        return s
