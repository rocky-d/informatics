from onlinejudge.leetcode import *


class H2O:
    def __init__(self) -> None:
        self.s_hydrogen = threading.Semaphore(2)
        self.s_oxygen = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        with self.s_hydrogen:
            self.barrier.wait()
            releaseHydrogen()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        with self.s_oxygen:
            self.barrier.wait()
            releaseOxygen()
