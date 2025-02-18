from onlinejudge.leetcode import *


class RangeFreqQuery:
    def __init__(self, arr: List[int]) -> None:
        idxes = defaultdict(lambda: [])
        for idx, num in enumerate(arr):
            idxes[num].append(idx)
        self.idxes = idxes

    def query(self, left: int, right: int, value: int) -> int:
        ls = self.idxes[value]
        return bisect_right(ls, right) - bisect_left(ls, left)
