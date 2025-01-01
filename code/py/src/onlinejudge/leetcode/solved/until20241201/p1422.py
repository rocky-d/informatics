class Solution:
    def maxScore(self, s: str) -> int:
        lft_0, rit_1 = [0], [0]
        for char in s[:-1]:
            lft_0.append(1 + lft_0[-1] if '0' == char else lft_0[-1])
        for char in s[:0:-1]:
            rit_1.insert(0, 1 + rit_1[0] if '1' == char else rit_1[0])
        del lft_0[0], rit_1[-1]
        return max(lft_0[i] + rit_1[i] for i in range(len(s) - 1))


eg_s = '011101'
print(Solution().maxScore(eg_s))
