from rockyutil.leetcode import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]


eg_s = ['h', 'e', 'l', 'l', 'o']
Solution().reverseString(eg_s)
print(eg_s)
