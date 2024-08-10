from onlinejudge.leetcode import *


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        s_counter, t_counter = Counter(s), Counter(t)
        for char, count in s_counter.items():
            ans += max(0, count - t_counter.get(char, 0))
        return ans
