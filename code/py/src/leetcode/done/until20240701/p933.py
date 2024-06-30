from rockyutil.leetcode import *


class RecentCounter:
    def __init__(self) -> None:
        self.que = deque(maxlen = 3001)

    def ping(self, t: int) -> int:
        t_3000 = t - 3000
        self.que.append(t)
        while self.que[0] < t_3000:
            self.que.popleft()
        return len(self.que)
