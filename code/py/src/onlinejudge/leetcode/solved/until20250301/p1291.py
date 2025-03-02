from onlinejudge.leetcode import *


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        start = int(str(low)[0])
        for i in range(len(str(low)), 1 + len(str(high))):
            for j in range(start, 11 - i):
                num = ''
                for k in range(j, j + i):
                    num += str(k)
                num = int(num)
                if num <= high:
                    ans.append(num)
            start = 1
        if 0 < len(ans) and ans[0] < low:
            del ans[0]
        return ans
