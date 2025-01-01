class Solution:
    def minEnd(self, n: int, x: int) -> int:
        zeros = x.bit_length() - x.bit_count()
        cyc = 1 << zeros
        a, b = divmod(n - 1, cyc)
        a, b = bin(a)[2:], bin(b)[2:]
        s = a
        b, i = '0' * (zeros - len(b)) + b, 0
        for bit in bin(x)[2:]:
            if '1' == bit:
                s += '1'
            else:  # elif '0' == bit:
                s += b[i]
                i += 1
        return int(s, base=2)


eg_n = 2
eg_x = 7
print(Solution().minEnd(eg_n, eg_x))
