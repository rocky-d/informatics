class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for char in s:
            if '(' == char:
                lo += 1
                hi += 1
            elif ')' == char:
                lo -= 1
                hi -= 1
            else:  # elif '*' == char:
                lo -= 1
                hi += 1
            if hi < 0:
                break
            if lo < 0:
                lo = 0
        return 0 == lo
