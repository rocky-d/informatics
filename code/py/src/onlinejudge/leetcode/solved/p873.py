from onlinejudge.leetcode import *


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        dp = {num: {} for num in arr}
        for i, num in enumerate(arr):
            for j in range(i):
                nxt = arr[j] + num
                if nxt in dp.keys():
                    dct = dp[nxt]
                    dct[num] = 2
            for lst, leng in dp[num].items():
                nxt = lst + num
                leng += 1
                if nxt in dp.keys():
                    dct = dp[nxt]
                    dct[num] = leng
                else:
                    ans = max(ans, leng)
        return ans


eg_arr = [2, 4, 8, 10, 14, 18, 32, 50]
print(Solution().lenLongestFibSubseq(eg_arr))
