from onlinejudge.leetcode import *


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ans = 0
        p0, p1 = pattern
        cnt_p0, cnt_p1 = 0, 0
        for char in text:
            if p1 == char:
                cnt_p1 += 1
                ans += cnt_p0
            if p0 == char:
                cnt_p0 += 1
        ans += max(cnt_p0, cnt_p1)
        return ans


eg_text = 'fyc'
eg_pattern = 'yy'
print(Solution().maximumSubsequenceCount(eg_text, eg_pattern))
