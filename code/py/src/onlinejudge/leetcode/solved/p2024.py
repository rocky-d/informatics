from onlinejudge.leetcode import *


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        prefs = list(accumulate((0 if 'F' == key else 1 for key in answerKey), initial=0))

        def check(mid: int) -> bool:
            for i in range(n - mid + 1):
                pref = prefs[i + mid] - prefs[i]
                if pref <= k or mid - k <= pref:
                    res = True
                    break
            else:
                res = False
            return res

        lo, hi = k - 1, n + 1
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if check(mid=mid):
                lo = mid
            else:
                hi = mid
        return lo


eg_answerKey = 'TTFTTFTT'
eg_k = 1
print(Solution().maxConsecutiveAnswers(eg_answerKey, eg_k))
