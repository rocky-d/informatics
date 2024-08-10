from onlinejudge.leetcode import *


class FizzBuzz:
    def __init__(self, n: int) -> None:
        self.n1 = n + 1
        self.s_fizz = threading.Semaphore(0)
        self.s_buzz = threading.Semaphore(0)
        self.s_fizzbuzz = threading.Semaphore(0)
        self.s_number = threading.Semaphore(1)

    def fizz(self, printFizz: Callable[[], None]) -> None:
        for i in range(3, self.n1, 3):
            if 0 == i % 15:
                continue
            self.s_fizz.acquire()
            printFizz()
            self.s_number.release()

    def buzz(self, printBuzz: Callable[[], None]) -> None:
        for i in range(5, self.n1, 5):
            if 0 == i % 15:
                continue
            self.s_buzz.acquire()
            printBuzz()
            self.s_number.release()

    def fizzbuzz(self, printFizzBuzz: Callable[[], None]) -> None:
        for i in range(15, self.n1, 15):
            self.s_fizzbuzz.acquire()
            printFizzBuzz()
            self.s_number.release()

    def number(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n1):
            self.s_number.acquire()
            is_times_3, is_times_5 = 0 == i % 3, 0 == i % 5
            if is_times_3 and not is_times_5:
                self.s_fizz.release()
            elif not is_times_3 and is_times_5:
                self.s_buzz.release()
            elif is_times_3 and is_times_5:
                self.s_fizzbuzz.release()
            else:
                printNumber(i)
                self.s_number.release()
