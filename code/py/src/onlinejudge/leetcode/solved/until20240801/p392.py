class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = True
        lent = len(t)
        ti = 0
        for si in range(len(s)):
            while ti < lent:
                if s[si] == t[ti]:
                    ti += 1
                    break
                else:
                    ti += 1
            else:
                ans = False
                break
        return ans
