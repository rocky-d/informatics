from rockyutil.leetcode import *


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        ans = 0
        w = word
        while True:
            ans += 1
            w = w[k:]
            if word.startswith(w):
                break
        return ans


eg_word = 'abcbabcd'
eg_k = 2
print(Solution().minimumTimeToInitialState(eg_word, eg_k))
