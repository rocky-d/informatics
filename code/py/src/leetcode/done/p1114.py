import threading


class Foo:
    def __init__(self):
        self.first_lock, self.second_lock = threading.Lock(), threading.Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_lock.acquire()
        printSecond()
        self.second_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_lock.acquire()
        printThird()
