from rockyutil.leetcode import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        half = len(s) // 2
        for lft, rit in zip(range(0, half, +1), range(-1, -1 - half, -1)):
            s[lft], s[rit] = s[rit], s[lft]


eg_s = ['h', 'e', 'l', 'l', 'o']
print(Solution().reverseString(eg_s))
