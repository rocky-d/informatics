from onlinejudge.leetcode import *


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        prefs = list(accumulate((1 if '0' == char else 0 for char in s), initial = 0))
        idxes = {}
        for idx, pref in enumerate(prefs):
            if pref not in idxes.keys():
                idxes[pref] = []
            idxes[pref].append(idx)
        for (a, a_ls), (b, b_ls) in combinations_with_replacement(idxes.items(), 2):
            tmp = (b - a) * (b - a + 1)
            for y in reversed(b_ls):
                if y < tmp:
                    break
                ans += bisect_right(a_ls, y - tmp)
        return ans - len(s) - 1


eg_s = '00011'
print(Solution().numberOfSubstrings(eg_s))

'''
x+y = n
y = n-x
x*x <= y
x*x <= n-x
x+x*x <= n
x*(x+1) <= n
'''
