class Solution:
    def longestAwesome(self, s: str) -> int:
        prefs = [0b0]
        for digit in map(int, s):
            prefs.append(prefs[-1] ^ 0b1 << digit)
        n = len(s)
        for length in range(n, 1, -1):
            if any((prefs[lft] ^ prefs[rit]).bit_count() <= 1 for lft, rit in zip(range(0, n - length + 1), range(length, n + 1))):
                ans = length
                break
        else:
            ans = 1
        return ans
