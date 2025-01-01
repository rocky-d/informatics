from onlinejudge.leetcode import *


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if 5 == bill:
                fives += 1
            elif 10 == bill:
                tens += 1
                if 1 <= fives:
                    fives -= 1
                else:
                    ans = False
                    break
            else:  # elif 20 == bill:
                if 1 <= tens and 1 <= fives:
                    tens -= 1
                    fives -= 1
                elif 3 <= fives:
                    fives -= 3
                else:
                    ans = False
                    break
        else:
            ans = True
        return ans
