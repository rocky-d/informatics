from rockyutil.leetcode import *


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        return list(sorted(((arr[lft] / arr[rit], (arr[lft], arr[rit])) for lft in range(n) for rit in range(lft + 1, n)), key = lambda item: item[0])[k - 1][1])
