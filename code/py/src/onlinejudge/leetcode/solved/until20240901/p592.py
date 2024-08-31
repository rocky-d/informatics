from onlinejudge.leetcode import *


class Solution:
    def fractionAddition(self, expression: str) -> str:
        ntor, dtor = 0, 1
        if '-' == expression[0]:
            expression = '0/1' + expression
        for group in expression.split('+'):
            group += '-0/1'
            frac, fracs = group.split('-', maxsplit=1)
            f_ntor, f_dtor = map(int, frac.split('/'))
            lcm_ = lcm(dtor, f_dtor)
            ntor *= lcm_ // dtor
            dtor = lcm_
            ntor += f_ntor * (lcm_ // f_dtor)
            for frac in fracs.split('-'):
                f_ntor, f_dtor = map(int, frac.split('/'))
                lcm_ = lcm(dtor, f_dtor)
                ntor *= lcm_ // dtor
                dtor = lcm_
                ntor -= f_ntor * (lcm_ // f_dtor)
        gcd_ = gcd(ntor, dtor)
        return f"{ntor // gcd_}/{dtor // gcd_}"


eg_expression = '1/3-1/2'
print(Solution().fractionAddition(eg_expression))
