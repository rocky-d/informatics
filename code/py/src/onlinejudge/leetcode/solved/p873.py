from onlinejudge.leetcode import *


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(lambda: set())
        for i, num in enumerate(arr):
            for leng, lst in dp[num]:
                dp[lst + num].add((leng + 1, num))
            for j in range(i):
                dp[arr[j] + num].add((2, num))
        leng = max(leng for val in dp.values() for leng, _ in val)
        return 0 if 2 == leng else leng


eg_arr = [2, 4, 8, 10, 14, 18, 32, 50]
print(Solution().lenLongestFibSubseq(eg_arr))
