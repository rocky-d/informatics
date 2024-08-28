from onlinejudge.leetcode import *


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = [0]
        default_factory = lambda: 0
        for minm in range(1, 1 + len(s)):
            cnter1, cnter2 = defaultdict(default_factory), defaultdict(default_factory)
            cnter2[0] = 27
            for i in reversed(range(minm)):
                char = s[i]
                cnter1_char = cnter1[char]
                cnter2[cnter1_char] -= 1
                if 0 == cnter2[cnter1_char]:
                    del cnter2[cnter1_char]
                cnter1[char] += 1
                cnter2[cnter1_char + 1] += 1
                if 2 == len(cnter2):
                    minm = min(minm, dp[i] + 1)
            dp.append(minm)
        return dp[-1]


eg_s = 'abababaccddb'
print(Solution().minimumSubstringsInPartition(eg_s))
