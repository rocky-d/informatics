from onlinejudge.leetcode import *


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        diff = ord('a') - 1
        s = ''.join(str(ord(char) - diff) for char in s)
        for _ in range(k):
            s = str(sum(map(int, s)))
        return int(s)
