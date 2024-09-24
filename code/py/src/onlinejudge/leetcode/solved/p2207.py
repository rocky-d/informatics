from onlinejudge.leetcode import *


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ans = 0
        x, y = pattern
        cnt_x, cnt_y = 0, 0
        for char in text:
            if y == char:
                cnt_y += 1
                ans += cnt_x
            if x == char:
                cnt_x += 1
        ans += max(cnt_x, cnt_y)
        return ans


eg_text = 'fyc'
eg_pattern = 'yy'
print(Solution().maximumSubsequenceCount(eg_text, eg_pattern))
