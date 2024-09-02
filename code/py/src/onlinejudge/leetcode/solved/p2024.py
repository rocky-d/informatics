from onlinejudge.leetcode import *


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        prefs = list(accumulate((0 if 'F' == key else 1 for key in answerKey), initial=0))
        n1 = len(prefs)

        def func(mid: int) -> int:
            mid_k = mid - k
            for i in range(mid, n1):
                pref = prefs[i] - prefs[i - mid]
                if pref <= k or mid_k <= pref:
                    res = 0
                    break
            else:
                res = 1
            return res

        return k + bisect_left(range(k, n1), 1, key=func) - 1


eg_answerKey = 'TTFTTFTT'
eg_k = 1
print(Solution().maxConsecutiveAnswers(eg_answerKey, eg_k))
