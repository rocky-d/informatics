from rockyutil.leetcode import *


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                ans = word
                break
        else:
            ans = ''
        return ans
