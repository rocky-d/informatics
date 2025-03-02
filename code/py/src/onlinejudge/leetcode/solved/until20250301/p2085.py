from onlinejudge.leetcode import *


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len(set(word for word, count in Counter(words1).items() if 1 == count) & set(word for word, count in Counter(words2).items() if 1 == count))
