class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = ''
        hh, mm = s.split(':')
        if '?' == hh[0]:
            ans += '1' if '0' == hh[1] or '1' == hh[1] or '?' == hh[1] else '0'
        else:
            ans += hh[0]
        if '?' == hh[1]:
            ans += '1' if '1' == hh[0] or '?' == hh[0] else '9'
        else:
            ans += hh[1]
        ans += ':'
        ans += '5' if '?' == mm[0] else mm[0]
        ans += '9' if '?' == mm[1] else mm[1]
        return ans
