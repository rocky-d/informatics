from onlinejudge.leetcode import *


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        for i, char in enumerate(s):
            if 1 == s_counter[char]:
                ans = i
                break
        else:
            ans = -1
        return ans
