from onlinejudge.leetcode import *


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ''
