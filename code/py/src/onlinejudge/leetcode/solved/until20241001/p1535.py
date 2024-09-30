from onlinejudge.leetcode import *


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) - 1 <= k:
            return max(arr)
        winner = arr.pop(0)
        idx, n = 0, len(arr)
        while True:
            cnt = 0
            while arr[idx] < winner:
                idx = (idx + 1) % n
                cnt += 1
                if cnt == k:
                    break
            else:
                arr[idx], winner = winner, arr[idx]
                continue
            break
        return winner


eg_arr = [2, 1, 3, 5, 4, 6, 7]
eg_k = 2
print(Solution().getWinner(eg_arr, eg_k))
