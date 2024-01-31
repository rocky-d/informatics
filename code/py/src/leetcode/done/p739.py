from rockyutil.leetcode import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in temperatures]
        stack_dec = [(-1, 101)]
        for i, temperature in enumerate(temperatures):
            while stack_dec[-1][1] < temperature:
                j = stack_dec.pop(-1)[0]
                ans[j] = i - j
            stack_dec.append((i, temperature))
        return ans
