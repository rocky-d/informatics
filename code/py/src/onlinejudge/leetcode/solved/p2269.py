class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        s = str(num)
        for i in range(len(s) - k + 1):
            divisor = int(s[i : i + k])
            if divisor and 0 == num % divisor:
                ans += 1
        return ans
