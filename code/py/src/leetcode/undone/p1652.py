from rockyutil.leetcode import *


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        n = len(code)
        rit = k + 1 if k > 0 else n
        k = abs(k)
        cnt = sum(code[rit - k: rit])
        for _ in range(n):
            ans.append(cnt)
            cnt += code[rit % n] - code[(rit - k) % n]
            rit += 1
        return ans
