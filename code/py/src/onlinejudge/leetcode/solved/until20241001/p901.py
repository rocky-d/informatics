from onlinejudge.leetcode import *


class StockSpanner:
    __slots__ = 'stk_dec'

    def __init__(self) -> None:
        self.stk_dec: Deque[Tuple[int, int]] = deque(((100_001, 0),))

    def next(self, price: int) -> int:
        cnt = 1
        while self.stk_dec[-1][0] <= price:
            cnt += self.stk_dec.pop()[1]
        self.stk_dec.append((price, cnt))
        return cnt
