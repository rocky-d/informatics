from onlinejudge.leetcode import *


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [word for word, cnt in Counter(chain(s1.split(' '), s2.split(' '))).items() if 1 == cnt]
