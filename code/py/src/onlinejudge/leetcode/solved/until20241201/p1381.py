class CustomStack:
    def __init__(self, maxSize: int) -> None:
        self.stk = [None] * maxSize
        self.ptr = 0
        self.lst = 0

    def push(self, x: int) -> None:
        if self.ptr == len(self.stk):
            return
        self.stk[self.ptr] = x - self.lst
        self.lst += self.stk[self.ptr]
        self.ptr += 1

    def pop(self) -> int:
        if 0 == self.ptr:
            return -1
        res = self.lst
        self.ptr -= 1
        self.lst -= self.stk[self.ptr]
        return res

    def increment(self, k: int, val: int) -> None:
        if 0 == self.ptr:
            return
        if self.ptr <= k:
            self.stk[0] += val
            self.lst += val
        else:
            self.stk[0] += val
            self.stk[k] -= val
