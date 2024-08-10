from onlinejudge.leetcode import *


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        ri_cnt1 = bank[0].count('1')
        for rj in bank[1:]:
            rj_cnt1 = rj.count('1')
            if 0 < rj_cnt1:
                ans += ri_cnt1 * rj_cnt1
                ri_cnt1 = rj_cnt1
        return ans


eg_bank = ['011001', '000000', '010100', '001000']
print(Solution().numberOfBeams(bank = eg_bank))
