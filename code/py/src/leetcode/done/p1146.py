from rockyutil.leetcode import *


class SnapshotArray:
    def __init__(self, length: int) -> None:
        self.snap_id = 0
        self.snap_array = [[(self.snap_id, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snap_array[index].append((self.snap_id, val))

    def snap(self) -> int:
        res = self.snap_id
        self.snap_id += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_array[index][bisect_right(self.snap_array[index], snap_id, key = lambda item: item[0]) - 1][1]
