from onlinejudge.leetcode import *


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def logical_not(arg):
            return not_(arg)

        def logical_and(*args):
            return reduce(and_, args)

        def logical_or(*args):
            return reduce(or_, args)

        return eval(
            expression.replace('t', 'True')
            .replace('f', 'False')
            .replace('!', 'logical_not')
            .replace('&', 'logical_and')
            .replace('|', 'logical_or')
        )
