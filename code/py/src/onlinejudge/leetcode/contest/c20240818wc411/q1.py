class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for length in range(1, len(s) + 1):
            for lft in range(len(s) - length + 1):
                cnt0 = s[lft:lft + length].count('0')
                cnt1 = length - cnt0
                if cnt0 <= k or cnt1 <= k:
                    ans += 1
        return ans


eg_s = '11111'
eg_k = 1
print(Solution().countKConstraintSubstrings(eg_s, eg_k))
