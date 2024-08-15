from onlinejudge.leetcode import *


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if 5 == bill:
                money[5] += 1
            elif 10 == bill:
                money[10] += 1
                if 1 <= money[5]:
                    money[5] -= 1
                else:
                    ans = False
                    break
            else:  # elif 20 == bill:
                money[20] += 1
                if 1 <= money[10] and 1 <= money[5]:
                    money[10] -= 1
                    money[5] -= 1
                elif 3 <= money[5]:
                    money[5] -= 3
                else:
                    ans = False
                    break
        else:
            ans = True
        return ans
