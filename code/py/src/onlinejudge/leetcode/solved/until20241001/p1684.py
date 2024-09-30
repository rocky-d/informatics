from onlinejudge.leetcode import *


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(1 for word in words if 0 == len(word.strip(allowed)))
