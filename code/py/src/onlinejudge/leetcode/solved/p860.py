from onlinejudge.leetcode import *


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if 5 == bill:
                change[5] += 1
            elif 10 == bill:
                change[10] += 1
                if 1 <= change[5]:
                    change[5] -= 1
                else:
                    ans = False
                    break
            else:  # elif 20 == bill:
                change[20] += 1
                if 1 <= change[10] and 1 <= change[5]:
                    change[10] -= 1
                    change[5] -= 1
                elif 3 <= change[5]:
                    change[5] -= 3
                else:
                    ans = False
                    break
        else:
            ans = True
        return ans
