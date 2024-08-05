from rockyutil.leetcode import *


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnter = Counter(arr)
        for s in arr:
            if 1 == cnter[s]:
                k -= 1
                if 0 == k:
                    ans = s
                    break
        else:
            ans = ''
        return ans
