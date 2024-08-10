from onlinejudge.leetcode import *


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0

        @cache
        def lcp(str1: str, str2: str):
            cnt = 0
            for char1, char2 in zip(str1, str2):
                if char1 == char2:
                    cnt += 1
                else:
                    break
            return cnt

        arr1_str, arr2_str = sorted(map(str, arr1), key = lambda s: len(s), reverse = True), sorted(map(str, arr2), key = lambda s: len(s), reverse = True)
        for str1 in arr1_str:
            for str2 in arr2_str:
                if ans < min(len(str1), len(str2)):
                    ans = max(ans, lcp(str1 = str1, str2 = str2))
        return ans
