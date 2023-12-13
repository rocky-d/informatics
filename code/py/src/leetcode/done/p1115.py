from rockyutil.leetcode import *


class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.BoundedSemaphore(1)
        self.s2 = threading.BoundedSemaphore(1)
        self.s2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.s2.acquire()
            printBar()
            self.s1.release()
