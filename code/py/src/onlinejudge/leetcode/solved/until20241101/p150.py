from onlinejudge.leetcode import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if '+' == token:
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif '-' == token:
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif '*' == token:
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif '/' == token:
                stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(token))
        return stack.pop(-1)


eg_tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
print(Solution().evalRPN(tokens = eg_tokens))
