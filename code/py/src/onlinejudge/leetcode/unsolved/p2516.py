from onlinejudge.leetcode import *


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if 0 == k:
            return 0
        cnt_a, cnt_b, cnt_c = 0, 0, 0
        for char in s:
            if 'a' == char:
                cnt_a += 1
            elif 'b' == char:
                cnt_b += 1
            else:  # elif 'c' == char:
                cnt_c += 1
        if not (k <= cnt_a and k <= cnt_b and k <= cnt_c):
            return -1

        def func(mid: int) -> int:
            range_mid1 = range(1 + mid)
            for lft, rit in zip(range_mid1, reversed(range_mid1)):
                cnt_a, cnt_b, cnt_c = 0, 0, 0
                for char in s[:lft] + (s[-rit:] if 0 < rit else ''):
                    if 'a' == char:
                        cnt_a += 1
                    elif 'b' == char:
                        cnt_b += 1
                    else:  # elif 'c' == char:
                        cnt_c += 1
                if k <= cnt_a and k <= cnt_b and k <= cnt_c:
                    res = 1
                    break
            else:
                res = 0
            return res

        return bisect_left(range(len(s) + 1), 1, lo=3 * k, key=func)


eg_s = 'aabaaaacaabc'
eg_k = 2
print(Solution().takeCharacters(eg_s, eg_k))
