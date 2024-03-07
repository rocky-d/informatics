from rockyutil.leetcode import *


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        num = 0
        for digit in map(lambda char: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[char], word):
            num = (digit + 10 * num) % m
            ans.append(1 if 0 == num else 0)
        return ans
