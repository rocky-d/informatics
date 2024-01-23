from rockyutil.leetcode import *


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = ['']
        for s in arr:
            if len(set(s)) < len(s):
                continue
            for prefix in dp.copy():
                new_s = prefix + s
                if len(set(new_s)) < len(new_s):
                    continue
                dp.append(new_s)
        return len(max(dp, key = len))


eg_arr = ['un', 'iq', 'ue']
print(Solution().maxLength(arr = eg_arr))
