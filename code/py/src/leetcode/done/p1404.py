class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        idx = len(s) - 1
        while '0' == s[idx]:
            idx -= 1
        idx += 1
        ans += len(s) - idx
        s = s[:idx]
        while '1' != s:
            idx = len(s) - 1
            while 0 <= idx and '1' == s[idx]:
                idx -= 1
            ans += len(s) - idx
            s = s[:idx] + '1' if 0 <= idx else '1'
        return ans
