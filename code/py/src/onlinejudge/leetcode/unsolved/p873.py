from onlinejudge.leetcode import *


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        for i, num in enumerate(arr):
            for lst, leng in dp[num].items():
                dct = dp[lst + num]
                dct[num] = max(dct[num], leng + 1)
            for j in range(i):
                dct = dp[arr[j] + num]
                dct[num] = max(dct[num], 2)
        leng = max(leng for dct in dp.values() for leng in dct.values())
        return 0 if 2 == leng else leng


eg_arr = [2, 4, 8, 10, 14, 18, 32, 50]
print(Solution().lenLongestFibSubseq(eg_arr))
