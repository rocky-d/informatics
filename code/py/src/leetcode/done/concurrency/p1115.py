from rockyutil.leetcode import *


class FooBar:
    def __init__(self, n) -> None:
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)

    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.s2.acquire()
            printBar()
            self.s1.release()
