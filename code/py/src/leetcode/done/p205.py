class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct, vals = dict(), set()
        for si, ti in zip(s, t):
            if si in dct.keys():
                if dct[si] != ti:
                    ans = False
                    break
            else:
                if ti in vals:
                    ans = False
                    break
                else:
                    dct[si] = ti
                    vals.add(ti)
        else:
            ans = True
        return ans
