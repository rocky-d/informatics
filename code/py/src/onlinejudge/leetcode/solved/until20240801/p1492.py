class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for factor in range(1, n + 1):
            if 0 == n % factor:
                k -= 1
                if 0 == k:
                    ans = factor
                    break
        else:
            ans = -1
        return ans
