from rockyutil.leetcode import *


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = ['']
        for s in arr:
            if len(s) == len(set(s)):
                dp.append(s)
                for prefix in dp[1:-1]:
                    new_s = prefix + s
                    if len(new_s) == len(set(new_s)):
                        dp.append(new_s)
        return len(max(dp, key = len))


eg_arr = ['un', 'iq', 'ue']
print(Solution().maxLength(arr = eg_arr))
