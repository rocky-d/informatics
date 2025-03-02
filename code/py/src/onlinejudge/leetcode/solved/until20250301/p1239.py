from onlinejudge.leetcode import *


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = ['']
        for s in arr:
            if len(s) == len(frozenset(s)):
                dp.append(s)
                for pre in dp[1:-1]:
                    new_s = pre + s
                    if len(new_s) == len(frozenset(new_s)):
                        dp.append(new_s)
        return len(max(dp, key = len))


eg_arr = ['un', 'iq', 'ue']
print(Solution().maxLength(arr = eg_arr))
