from onlinejudge.leetcode import *


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        cnters = list(map(Counter, words))
        for char in reduce(and_, (cnter.keys() for cnter in cnters)):
            cnt = inf
            for cnter in cnters:
                cnt = min(cnt, cnter[char])
            ans += [char] * cnt
        return ans
