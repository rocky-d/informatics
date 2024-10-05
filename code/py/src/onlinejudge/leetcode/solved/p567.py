from onlinejudge.leetcode import *


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1) - 1
        s1_cnter, cnter = Counter(s1), Counter(s2[:n])
        for lft, rit in zip(range(0, len(s2) - n), range(n, len(s2))):
            cnter[s2[rit]] += 1
            if all(cnt == cnter[char] for char, cnt in s1_cnter.items()):
                ans = True
                break
            cnter[s2[lft]] -= 1
        else:
            ans = False
        return ans
