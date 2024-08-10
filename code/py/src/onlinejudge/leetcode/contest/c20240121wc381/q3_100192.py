from onlinejudge.leetcode import *


class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        buttons = 8
        for count in sorted(Counter(word).values(), reverse = True):
            ans += count * (buttons // 8)
            buttons += 1
        return ans


eg_word = 'aabbccddeeffgghhiiiiii'
print(Solution().minimumPushes(word = eg_word))
