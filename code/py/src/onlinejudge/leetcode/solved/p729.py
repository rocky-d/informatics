from onlinejudge.leetcode import *


class MyCalendar:
    def __init__(self) -> None:
        self.lfts = sc.SortedList()
        self.rits = sc.SortedList()

    def book(self, start: int, end: int) -> bool:
        if self.rits.bisect_right(start) == self.lfts.bisect_left(end):
            self.lfts.add(start)
            self.rits.add(end)
            res = True
        else:
            res = False
        return res
