from rockyutil.leetcode import *


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ans = inf
        vals = sorted(Counter(word).values(), reverse = True)
        prefs = [0]
        for val in vals:
            prefs.append(prefs[-1] + val)
        val_base = 0
        idx = len(vals) - 1
        for val in reversed(vals):
            line = val + k
            while 0 <= idx and vals[idx] <= line:
                idx -= 1
            ans = min(ans, val_base + prefs[idx + 1] - line * (idx + 1))
            val_base += val
        return ans


eg_word = 'aabcaba'
eg_k = 0
print(Solution().minimumDeletions(eg_word, eg_k))
