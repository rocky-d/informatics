from rockyutil.leetcode import *


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)
        self.s3 = threading.Semaphore(0)
        self.count = 0

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.count < self.n:
            self.s1.acquire()
            printNumber(0)
            self.count += 1
            if 0 == self.count % 2:
                self.s2.release()
            else:  # 1 == self.count % 2:
                self.s3.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(2, self.n + 1, 2):
            self.s2.acquire()
            printNumber(self.count)
            self.s1.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(1, self.n + 1, 2):
            self.s3.acquire()
            printNumber(self.count)
            self.s1.release()


def eg_printNumber(number: int) -> None:
    print(number, end = '')


eg_n = 5
instance = ZeroEvenOdd(n = eg_n)

threads = [
    threading.Thread(target = instance.zero, args = (eg_printNumber,)),
    threading.Thread(target = instance.even, args = (eg_printNumber,)),
    threading.Thread(target = instance.odd, args = (eg_printNumber,)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
