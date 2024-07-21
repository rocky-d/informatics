class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n < k:
            return -1
        ans = 0
        n = bin(n)[2:]
        k = bin(k)[2:].zfill(len(n))
        for i in range(len(n)):
            if '0' == n[i] and '1' == k[i]:
                ans = -1
                break
            if '1' == n[i] and '0' == k[i]:
                ans += 1
        return ans
