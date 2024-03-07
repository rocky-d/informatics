from rockyutil.leetcode import *


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        num = 0
        for digit in map(int, word):
            num = digit + 10 * num
            ans.append(1 if 0 == num % m else 0)
        return ans
