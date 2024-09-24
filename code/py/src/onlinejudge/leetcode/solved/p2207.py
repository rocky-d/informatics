from onlinejudge.leetcode import *


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        x, y = pattern
        prefs = list(accumulate((1 if x == char else 0 for char in text), initial=0))
        return sum(prefs[i] for i in reversed(range(len(text))) if y == text[i]) + max(prefs[-1], text.count(y))


eg_text = 'fyc'
eg_pattern = 'yy'
print(Solution().maximumSubsequenceCount(eg_text, eg_pattern))
