from onlinejudge.leetcode import *


class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        for c, group in groupby(s):
            if 'P' == c:
                continue
            cnt = len(list(group))
            if 'A' == c:
                absents += cnt
                if 2 <= absents:
                    ans = False
                    break
            elif 'L' == c and 3 <= cnt:
                ans = False
                break
        else:
            ans = True
        return ans
