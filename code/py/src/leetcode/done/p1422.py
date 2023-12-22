class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros, right_ones = [0], [0]
        for char in s[:-1]:
            left_zeros.append(1 + left_zeros[-1] if '0' == char else left_zeros[-1])
        for char in reversed(s[1:]):
            right_ones.insert(0, 1 + right_ones[0] if '1' == char else right_ones[0])
        del left_zeros[0], right_ones[-1]
        ans = 0
        for i in range(len(s) - 1):
            ans = max(ans, left_zeros[i] + right_ones[i])
        return ans


eg_s = '011101'
print(Solution().maxScore(s = eg_s))
