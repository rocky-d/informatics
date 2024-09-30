from onlinejudge.leetcode import *


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(char * cnt for char, cnt in sorted(Counter(s).items(), key = lambda item: item[1], reverse = True))
