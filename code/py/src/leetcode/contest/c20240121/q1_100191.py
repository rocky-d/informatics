from rockyutil.leetcode import *


class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        buttons = 8
        for char, count in sorted(Counter(word).items(), key = lambda item: item[1], reverse = True):
            ans += count * (buttons // 8)
            buttons += 1
        return ans


eg_word = 'abcde'
print(Solution().minimumPushes(word = eg_word))
