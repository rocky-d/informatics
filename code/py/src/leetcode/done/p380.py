from rockyutil.leetcode import *


class RandomizedSet:
    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        if val in self._set:
            res = False
        else:  # elif val not in self._set:
            res = True
            self._set.add(val)
        return res

    def remove(self, val: int) -> bool:
        if val in self._set:
            res = True
            self._set.remove(val)
        else:  # elif val not in self._set:
            res = False
        return res

    def getRandom(self) -> int:
        return choice(tuple(self._set))
