from rockyutil.leetcode import *


class RandomizedSet:
    def __init__(self):
        self._list = list()
        self._dict = dict()

    def insert(self, val: int) -> bool:
        if val in self._dict.keys():
            res = False
        else:  # elif val not in self._dict.keys():
            res = True
            self._dict[val] = len(self._list)
            self._list.append(val)
        return res

    def remove(self, val: int) -> bool:
        if val in self._dict.keys():
            res = True
            val_index = self._dict[val]
            self._list[val_index] = self._list[-1]
            self._dict[self._list[-1]] = val_index
            del self._list[-1]
            del self._dict[val]
        else:  # elif val not in self._dict.keys():
            res = False
        return res

    def getRandom(self) -> int:
        return choice(self._list)
