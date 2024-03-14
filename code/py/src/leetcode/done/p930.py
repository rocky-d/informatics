from rockyutil.leetcode import *


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        prefs = [0]
        prefs_cnter = Counter(prefs)
        for num in nums:
            prefs.append(prefs[-1] + num)
            ans += prefs_cnter[prefs[-1] - goal]
            prefs_cnter[prefs[-1]] += 1
        return ans
