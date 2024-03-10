from rockyutil.leetcode import *


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        chars1, chars2 = Counter(), Counter()
        for char1, char2 in zip(secret, guess):
            if char1 == char2:
                bulls += 1
            else:
                chars1[char1] += 1
                chars2[char2] += 1
        return f"{bulls}A{sum(min(chars1[char], chars2[char]) for char in chars1)}B"
