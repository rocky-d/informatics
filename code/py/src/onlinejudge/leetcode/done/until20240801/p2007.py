from onlinejudge.leetcode import *


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        cnter = Counter(changed)
        for num in sorted(changed):
            num2 = num + num
            while 0 < cnter[num]:
                cnter[num] -= 1
                if 0 < cnter[num2]:
                    cnter[num2] -= 1
                    ans.append(num)
                else:
                    ans = []
                    break
            else:
                continue
            break
        return ans
