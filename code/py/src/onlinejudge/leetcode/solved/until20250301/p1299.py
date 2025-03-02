from onlinejudge.leetcode import *


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.append(-1)
        del arr[0]
        for i in range(len(arr) - 2, -1, -1):
            arr[i] = max(arr[i], arr[i + 1])
        return arr
