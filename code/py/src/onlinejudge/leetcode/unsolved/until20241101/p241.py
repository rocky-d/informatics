from onlinejudge.leetcode import *
from operator import add, sub, mul


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {'+': add, '-': sub, '*': mul}
        dp = [[0]]
        expression = '+' + expression
        i, n = 0, len(expression)
        while i < n:
            op = ops[expression[i]]
            num = ''
            i += 1
            while i < n and expression[i].isdigit():
                num += expression[i]
                i += 1
            num = int(num)
            ls = []
            for val in dp[-1]:
                ls.append(op(val, num))
            if 2 <= len(dp):
                num1 = op(lst[1], num)
                for val in dp[-2]:
                    ls.append(lst[0](val, num1))
            lst = op, num
            dp.append(ls)
        print(dp)
        return dp[-1]


eg_expression = '2*3-4*5'
print(Solution().diffWaysToCompute(eg_expression))
