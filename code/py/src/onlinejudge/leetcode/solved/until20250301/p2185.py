from onlinejudge.leetcode import *


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))
