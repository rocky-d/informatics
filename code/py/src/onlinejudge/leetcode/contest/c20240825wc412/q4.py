from onlinejudge.leetcode import *


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        cnter = Counter(nums)
        for cnt in cnter.values():
            ans += comb(cnt, 2)
        for (x, x_cnt), (y, y_cnt) in combinations(cnter.items(), r=2):
            x, y = str(x), str(y)
            if len(x) < len(y):
                x = "0" * (len(y) - len(x)) + x
            elif len(y) < len(x):
                y = "0" * (len(x) - len(y)) + y
            ls = []
            for xi, yi in zip(x, y):
                if xi != yi:
                    ls.append((xi, yi))
                    if 4 < len(ls):
                        break
            else:
                if 2 == len(ls) and ls[0][0] == ls[1][1] and ls[1][0] == ls[0][1]:
                    ans += x_cnt * y_cnt
                elif 3 == len(ls) and (
                    ls[0][0] == ls[1][1]
                    and ls[1][0] == ls[2][1]
                    and ls[2][0] == ls[0][1]
                    or ls[0][0] == ls[2][1]
                    and ls[1][0] == ls[0][1]
                    and ls[2][0] == ls[1][1]
                ):
                    ans += x_cnt * y_cnt
                elif 4 == len(ls) and (
                    ls[0][0] == ls[1][1]
                    and ls[1][0] == ls[0][1]
                    and ls[2][0] == ls[3][1]
                    and ls[3][0] == ls[2][1]
                    or ls[0][0] == ls[2][1]
                    and ls[1][0] == ls[3][1]
                    and ls[2][0] == ls[0][1]
                    and ls[3][0] == ls[1][1]
                    or ls[0][0] == ls[3][1]
                    and ls[1][0] == ls[2][1]
                    and ls[2][0] == ls[1][1]
                    and ls[3][0] == ls[0][1]
                ):
                    ans += x_cnt * y_cnt
        return ans
