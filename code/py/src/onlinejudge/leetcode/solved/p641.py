from onlinejudge.leetcode import *


class MyCircularDeque:
    def __init__(self, k: int) -> None:
        self.que = [None] + [None] * k
        self.n = len(self.que)
        self.lft = 0
        self.rit = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[self.rit] = value
        self.rit += 1
        self.rit %= self.n
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.lft -= 1
        self.lft %= self.n
        self.que[self.lft] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.rit -= 1
        self.rit %= self.n
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.lft += 1
        self.lft %= self.n
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.que[(self.rit - 1) % self.n]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.que[self.lft]

    def isEmpty(self) -> bool:
        return self.lft == self.rit

    def isFull(self) -> bool:
        return self.lft == (self.rit + 1) % self.n
