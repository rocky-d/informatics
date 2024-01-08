from rockyutil.leetcode import *


class DiningPhilosophers:
    def __init__(self):
        self.dining = threading.Semaphore(4)
        self.forks = [threading.Semaphore(1) for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left_fork, right_fork = philosopher % 5, (philosopher + 1) % 5
        self.dining.acquire()
        self.forks[left_fork].acquire()
        self.forks[right_fork].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()
        self.forks[right_fork].release()
        self.forks[left_fork].release()
        self.dining.release()


eg_n = 1
instance = DiningPhilosophers()

for _ in range(eg_n):
    threads = [
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                0,
                lambda: print([0, 1, 1]),
                lambda: print([0, 2, 1]),
                lambda: print([0, 0, 3]),
                lambda: print([0, 1, 2]),
                lambda: print([0, 2, 2]),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                1,
                lambda: print([1, 1, 1]),
                lambda: print([1, 2, 1]),
                lambda: print([1, 0, 3]),
                lambda: print([1, 1, 2]),
                lambda: print([1, 2, 2]),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                2,
                lambda: print([2, 1, 1]),
                lambda: print([2, 2, 1]),
                lambda: print([2, 0, 3]),
                lambda: print([2, 1, 2]),
                lambda: print([2, 2, 2]),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                3,
                lambda: print([3, 1, 1]),
                lambda: print([3, 2, 1]),
                lambda: print([3, 0, 3]),
                lambda: print([3, 1, 2]),
                lambda: print([3, 2, 2]),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                4,
                lambda: print([4, 1, 1]),
                lambda: print([4, 2, 1]),
                lambda: print([4, 0, 3]),
                lambda: print([4, 1, 2]),
                lambda: print([4, 2, 2]),
            ),
        ),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
