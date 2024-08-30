from onlinejudge.leetcode import *


class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        mid = n >> 1
        if 0b1 == 0b1 & n:
            text = text[:mid] + text[mid] + text[mid:]
            n += 1
            mid += 1
            dp = [1] * mid + [-1]
        else:
            dp = [1] * mid + [0]
        for i in range(1, mid + 1):
            lft, rit = mid - i, mid + i
            for j in range(1, i + 1):
                if text[lft : lft + j] == text[rit - j : rit]:
                    dp[lft] = dp[lft + j] + 2
                    break
        return dp[0]


eg_text = 'ghiabcdefhelloadamhelloabcdefghi'
print(Solution().longestDecomposition(eg_text))
