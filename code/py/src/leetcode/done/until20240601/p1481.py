from rockyutil.leetcode import *


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_cnter = sorted(Counter(arr).items(), key = lambda item: item[1])
        ans = len(arr_cnter)
        for _, cnt in arr_cnter:
            if k < cnt:
                break
            else:
                k -= cnt
                ans -= 1
        return ans
