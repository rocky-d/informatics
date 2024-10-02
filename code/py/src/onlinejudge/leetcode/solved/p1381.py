from onlinejudge.leetcode import *


class CustomStack:
    def __init__(self, maxSize: int) -> None:
        self.stk = [None] * maxSize
        self.ptr = 0

    def push(self, x: int) -> None:
        if self.ptr == len(self.stk):
            return
        self.stk[self.ptr] = x
        self.ptr += 1

    def pop(self) -> int:
        if 0 == self.ptr:
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.ptr, k)):
            self.stk[i] += val
