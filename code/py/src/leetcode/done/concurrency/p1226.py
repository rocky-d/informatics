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
