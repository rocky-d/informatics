from rockyutil.leetcode import *


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ans = 0
        m = len(pattern)
        nxts = [0]
        lft = 0
        for rit in range(1, m):
            patt_rit = pattern[rit]
            while pattern[lft] != patt_rit and 0 < lft:
                lft = nxts[lft - 1]
            if pattern[lft] == patt_rit:
                lft += 1
            nxts.append(lft)
        j = 0
        for a, b in pairwise(nums):
            val = 1 if a < b else 0 if a == b else -1
            while val != pattern[j] and 0 < j:
                j = nxts[j - 1]
            if val == pattern[j]:
                j += 1
                if j == m:
                    ans += 1
                    j = nxts[-1]
        return ans
