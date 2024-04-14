class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = ''
        h, m = s.split(':')
        if '?' == h[0]:
            ans += '1' if '0' == h[1] or '1' == h[1] or '?' == h[1] else '0'
        else:
            ans += h[0]
        if '?' == h[1]:
            ans += '1' if '1' == h[0] or '?' == h[0] else '9'
        else:
            ans += h[1]
        ans += ':'
        ans += '5' if '?' == m[0] else m[0]
        ans += '9' if '?' == m[1] else m[1]
        return ans
