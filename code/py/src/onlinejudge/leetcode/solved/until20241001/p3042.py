from onlinejudge.leetcode import *


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0

        @cache
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if len(str2) < len(str1):
                res = False
            elif len(str2) == len(str1):
                res = str1 == str2
            else:
                res = str2.startswith(str1) and str2.endswith(str1)
            return res

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(str1 = words[i], str2 = words[j]):
                    ans += 1
        return ans
