from rockyutil.leetcode import *


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if '../' == log:
                if 0 < ans:
                    ans -= 1
            elif './' == log:
                pass
            else:
                ans += 1
        return ans
