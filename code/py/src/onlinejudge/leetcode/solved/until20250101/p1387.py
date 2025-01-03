class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ls = [(-1, 0)]
        for x in range(lo, hi + 1):
            x_ = x
            cnt = 0
            while 1 < x:
                cnt += 1
                if 0b0 == 0b1 & x:
                    x >>= 1
                else:  # elif 0b1 == 0b1 & x:
                    x = 3 * x + 1
            ls.append((cnt, x_))
        return sorted(ls)[k][1]
