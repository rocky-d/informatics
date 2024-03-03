from rockyutil.leetcode import *


class MyQueue:
    def __init__(self) -> None:
        self.stk1 = deque()
        self.stk2 = deque()

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        if 0 == len(self.stk2):
            for _ in range(len(self.stk1)):
                self.stk2.append(self.stk1.pop())
        return self.stk2.pop()

    def peek(self) -> int:
        if 0 == len(self.stk2):
            for _ in range(len(self.stk1)):
                self.stk2.append(self.stk1.pop())
        return self.stk2[-1]

    def empty(self) -> bool:
        return 0 == len(self.stk1) == len(self.stk2)
