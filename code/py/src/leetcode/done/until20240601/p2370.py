class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        oft = ord('a')
        for char in s:
            num = ord(char) - oft
            dp[num] = 1 + max(dp[max(0, num - k): num + k + 1])
        return max(dp)
