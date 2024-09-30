from onlinejudge.leetcode import *


class SeatManager:
    def __init__(self, n: int) -> None:
        self.seats = list(range(1, 1 + n))

    def reserve(self) -> int:
        return heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)
