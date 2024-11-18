from onlinejudge.leetcode import *


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if 0 == k:
            return [0] * n
        ans = []
        lft, rit = (1, k) if 0 < k else (n + k, n - 1)
        cnt = sum(code[lft : rit + 1])
        for _ in range(n):
            ans.append(cnt)
            cnt -= code[lft]
            lft = (lft + 1) % n
            rit = (rit + 1) % n
            cnt += code[rit]
        return ans
