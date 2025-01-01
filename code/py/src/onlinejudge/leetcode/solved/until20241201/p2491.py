from onlinejudge.leetcode import *


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pair, mod = divmod(sum(skill), len(skill) // 2)
        if 0 != mod:
            return -1
        ans = 0
        cnter = sorted(Counter(sorted(skill)).items(), key=lambda item: item[0])
        lft, rit = 0, len(cnter) - 1
        while lft < rit:
            if pair == cnter[lft][0] + cnter[rit][0] and cnter[lft][1] == cnter[rit][1]:
                ans += cnter[lft][0] * cnter[rit][0] * cnter[lft][1]
                lft += 1
                rit -= 1
            else:
                ans = -1
                break
        else:
            if lft == rit:
                if pair == cnter[lft][0] + cnter[rit][0] and 0b0 == 0b1 & cnter[lft][1]:
                    ans += cnter[lft][0] * cnter[rit][0] * (cnter[lft][1] >> 1)
                else:
                    ans = -1
        return ans
