from rockyutil.leetcode import *


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        for key, val in Counter(Counter(tasks).values()).items():
            if 1 == key:
                ans = -1
                break
            else:
                ans += val * (key // 3 if 0 == key % 3 else key // 3 + 1)
        return ans
