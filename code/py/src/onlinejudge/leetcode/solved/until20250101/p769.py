from onlinejudge.leetcode import *


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        i, n = 0, len(arr)
        while i < n:
            maxm = arr[i]
            while i < maxm:
                i += 1
                maxm = max(maxm, arr[i])
            i += 1
            ans += 1
        return ans


eg_arr = [1, 2, 0, 3]
print(Solution().maxChunksToSorted(eg_arr))
