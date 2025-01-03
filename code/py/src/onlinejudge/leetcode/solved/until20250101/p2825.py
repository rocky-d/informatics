from onlinejudge.leetcode import *


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        i, n = 0, len(str2)
        for char in str1:
            if str2[i] == char or str2[i] == chr((ord(char) - 96) % 26 + 97):
                i += 1
                if i == n:
                    ans = True
                    break
        else:
            ans = False
        return ans
