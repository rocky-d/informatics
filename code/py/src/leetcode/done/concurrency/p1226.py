from rockyutil.leetcode import *


class DiningPhilosophers:
    def __init__(self) -> None:
        self.dining = threading.Semaphore(4)
        self.forks = [threading.Semaphore(1) for _ in range(5)]

    def wantsToEat(
            self,
            philosopher: int,
            pickLeftFork: Callable[[], None],
            pickRightFork: Callable[[], None],
            eat: Callable[[], None],
            putLeftFork: Callable[[], None],
            putRightFork: Callable[[], None],
    ) -> None:
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


eg_n = 2
instance = DiningPhilosophers()

for _ in range(eg_n):
    threads = [
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                0,
                lambda: print('[0, 1, 1] 0号哲学家拿起了左边的叉子\n', end = ''),
                lambda: print('[0, 2, 1] 0号哲学家拿起了右边的叉子\n', end = ''),
                lambda: print('[0, 0, 3] 0号哲学家吃了面\n', end = ''),
                lambda: print('[0, 1, 2] 0号哲学家放下了左边的叉子\n', end = ''),
                lambda: print('[0, 2, 2] 0号哲学家放下了右边的叉子\n', end = ''),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                1,
                lambda: print('[1, 1, 1] 1号哲学家拿起了左边的叉子\n', end = ''),
                lambda: print('[1, 2, 1] 1号哲学家拿起了右边的叉子\n', end = ''),
                lambda: print('[1, 0, 3] 1号哲学家吃了面\n', end = ''),
                lambda: print('[1, 1, 2] 1号哲学家放下了左边的叉子\n', end = ''),
                lambda: print('[1, 2, 2] 1号哲学家放下了右边的叉子\n', end = ''),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                2,
                lambda: print('[2, 1, 1] 2号哲学家拿起了左边的叉子\n', end = ''),
                lambda: print('[2, 2, 1] 2号哲学家拿起了右边的叉子\n', end = ''),
                lambda: print('[2, 0, 3] 2号哲学家吃了面\n', end = ''),
                lambda: print('[2, 1, 2] 2号哲学家放下了左边的叉子\n', end = ''),
                lambda: print('[2, 2, 2] 2号哲学家放下了右边的叉子\n', end = ''),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                3,
                lambda: print('[3, 1, 1] 3号哲学家拿起了左边的叉子\n', end = ''),
                lambda: print('[3, 2, 1] 3号哲学家拿起了右边的叉子\n', end = ''),
                lambda: print('[3, 0, 3] 3号哲学家吃了面\n', end = ''),
                lambda: print('[3, 1, 2] 3号哲学家放下了左边的叉子\n', end = ''),
                lambda: print('[3, 2, 2] 3号哲学家放下了右边的叉子\n', end = ''),
            ),
        ),
        threading.Thread(
            target = instance.wantsToEat,
            args = (
                4,
                lambda: print('[4, 1, 1] 4号哲学家拿起了左边的叉子\n', end = ''),
                lambda: print('[4, 2, 1] 4号哲学家拿起了右边的叉子\n', end = ''),
                lambda: print('[4, 0, 3] 4号哲学家吃了面\n', end = ''),
                lambda: print('[4, 1, 2] 4号哲学家放下了左边的叉子\n', end = ''),
                lambda: print('[4, 2, 2] 4号哲学家放下了右边的叉子\n', end = ''),
            ),
        ),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
