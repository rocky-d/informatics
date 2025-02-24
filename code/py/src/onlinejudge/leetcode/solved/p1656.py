from onlinejudge.leetcode import *


class OrderedStream:
    def __init__(self, n: int) -> None:
        self.values = [None] + [None] * n + [None]
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        values = self.values
        ptr = self.ptr
        values[idKey] = value
        while values[ptr] is not None:
            res.append(values[ptr])
            ptr += 1
        self.ptr = ptr
        return res
