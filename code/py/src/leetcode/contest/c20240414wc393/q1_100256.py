class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = ''
        h, m = s.split(':')
        if h[0] == '?':
            if h[1] == '0' or h[1] == '1' or h[1] == '?':
                ans += '1'
            else:
                ans += '0'
        else:
            ans += h[0]
        if '?' == h[1]:
            if ans[0] == '1':
                ans += '1'
            else:
                ans += '9'
        else:
            ans += h[1]
        ans += ':'
        ans += '5' if '?' == m[0] else m[0]
        ans += '9' if '?' == m[1] else m[1]
        return ans
