from onlinejudge.leetcode import *


class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        buttons = 8
        for cnt in sorted(Counter(word).values(), reverse = True):
            ans += cnt * (buttons // 8)
            buttons += 1
        return ans


eg_word = 'aabbccddeeffgghhiiiiii'
print(Solution().minimumPushes(word = eg_word))
