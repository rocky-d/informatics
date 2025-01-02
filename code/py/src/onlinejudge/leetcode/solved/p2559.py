from onlinejudge.leetcode import *


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = frozenset('aeiou')
        prefs = list(accumulate((1 if word[0] in vowels and word[-1] in vowels else 0 for word in words), initial=0))
        return [prefs[rit + 1] - prefs[lft] for lft, rit in queries]
