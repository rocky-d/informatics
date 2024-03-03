from rockyutil.leetcode import *


class MyStack:
    def __init__(self) -> None:
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        self.que1.append(x)

    def pop(self) -> int:
        self.que1, self.que2 = self.que2, self.que1
        while 1 < len(self.que2):
            self.que1.append(self.que2.popleft())
        return self.que2.popleft()

    def top(self) -> int:
        self.que1, self.que2 = self.que2, self.que1
        while 1 < len(self.que2):
            self.que1.append(self.que2.popleft())
        self.que1.append(self.que2[0])
        return self.que2.popleft()

    def empty(self) -> bool:
        return 0 == len(self.que1)
