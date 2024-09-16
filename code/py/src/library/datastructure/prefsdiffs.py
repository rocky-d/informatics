from itertools import pairwise


class _PrefsDiffs(object):

    def __init__(self, __start):
        self._start = __start

    @property
    def start(self):
        return self._start


class _Prefs(_PrefsDiffs):

    def __init__(self, __start):
        super().__init__(__start)
        self._prefs = None

    @property
    def prefs(self):
        return self._prefs

    def sum(self, *args, **kwargs):
        pass


class _Diffs(_PrefsDiffs):

    def __init__(self, __start):
        super().__init__(__start)
        self._diffs = None

    @property
    def diffs(self):
        return self._diffs

    def add(self, *args, **kwargs):
        pass


class Prefs1D(_Prefs):

    def __init__(self, __tensor1d, start = 0):
        super().__init__(start)
        self._prefs = [...] + [...] * len(__tensor1d)
        self._prefs[0] = self._start
        for i0d, x0d in enumerate(__tensor1d, start = 1):
            self._prefs[i0d] = x0d + self._prefs[i0d - 1]

    def sum(self, lo, hi):  # [lo, hi]
        hi = hi + 1
        return self._prefs[hi] - self._prefs[lo]


class Diffs1D(_Diffs):

    def __init__(self, __tensor1d, start = 0):
        super().__init__(start)
        self._diffs = [...] * len(__tensor1d)
        self._diffs[0] = __tensor1d[0] - self._start
        for i0d, (lst0d, nxt0d) in enumerate(pairwise(__tensor1d), start = 1):
            self._diffs[i0d] = nxt0d - lst0d

    def add(self, lo, hi, val):  # [lo, hi]
        self._diffs[lo] += val
        hi = hi + 1
        if hi < len(self._diffs):
            self._diffs[hi] -= val


class Prefs2D(_Prefs):

    def __init__(self, __tensor2d, start = 0):
        super().__init__(start)
        self._prefs = [...] + [...] * len(__tensor2d)
        self._prefs[0] = [...] + [...] * len(__tensor2d[0])
        self._prefs[0][0] = self._start
        for i0d in range(1, 1 + len(__tensor2d[0])):
            self._prefs[0][i0d] = self._start
        for i1d, x1d in enumerate(__tensor2d, start = 1):
            self._prefs[i1d] = [...] + [...] * len(__tensor2d[0])
            self._prefs[i1d][0] = self._start
            for i0d, x0d in enumerate(x1d, start = 1):
                self._prefs[i1d][i0d] = x0d - self._prefs[i1d - 1][i0d - 1] + self._prefs[i1d - 1][i0d] + self._prefs[i1d][i0d - 1]

    def sum(self, lo, hi):  # [lo, hi]
        hi = hi[0] + 1, hi[1] + 1
        return self._prefs[hi[0]][hi[1]] + self._prefs[lo[0]][lo[1]] - self._prefs[lo[0]][hi[1]] - self._prefs[hi[0]][lo[1]]


class Diffs2D(_Diffs):

    def __init__(self, __tensor2d, start = 0):
        super().__init__(start)
        self._diffs = [...] * len(__tensor2d)
        self._diffs[0] = [...] * len(__tensor2d[0])
        self._diffs[0][0] = __tensor2d[0][0] - self._start
        for i0d, (lst0d, nxt0d) in enumerate(pairwise(__tensor2d[0]), start = 1):
            self._diffs[0][i0d] = nxt0d - lst0d
        for i1d, (lst1d, nxt1d) in enumerate(pairwise(__tensor2d), start = 1):
            self._diffs[i1d] = [...] * len(__tensor2d[0])
            self._diffs[i1d][0] = nxt1d[0] - lst1d[0]
            for i0d, ((lst1d_lst0d, lst1d_nxt0d), (nxt1d_lst0d, nxt1d_nxt0d)) in enumerate(zip(pairwise(lst1d), pairwise(nxt1d)), start = 1):
                self._diffs[i1d][i0d] = nxt1d_nxt0d + lst1d_lst0d - lst1d_nxt0d - nxt1d_lst0d

    def add(self, lo, hi, val):  # [lo, hi]
        self._diffs[lo[0]][lo[1]] += val
        hi = hi[0] + 1, hi[1] + 1
        if hi[0] < len(self._diffs) and hi[1] < len(self._diffs[0]):
            self._diffs[hi[0]][hi[1]] += val
        if hi[0] < len(self._diffs):
            self._diffs[hi[0]][lo[1]] -= val
        if hi[1] < len(self._diffs[0]):
            self._diffs[lo[0]][hi[1]] -= val


if __name__ == '__main__':
    print2d = lambda __iterable: print(*__iterable, sep = '\n', end = '\n\n')

    tensor1d = [1, 2, 3, 4, 5]
    print(tensor1d)
    print(Prefs1D(tensor1d, start = 0).prefs)
    print(Diffs1D(tensor1d, start = 0).diffs)
    print(Diffs1D(Prefs1D(tensor1d, start = 0).prefs, start = 0).diffs)
    print(Prefs1D(Diffs1D(tensor1d, start = 0).diffs, start = 0).prefs)
    print('------')

    tensor2d = [
        [1, 2, 3],
        [5, 5, 3],
        [8, 2, 4],
    ]
    print2d(tensor2d)
    print2d(Prefs2D(tensor2d, start = 0).prefs)
    print2d(Diffs2D(tensor2d, start = 0).diffs)
    print2d(Diffs2D(Prefs2D(tensor2d, start = 0).prefs, start = 0).diffs)
    print2d(Prefs2D(Diffs2D(tensor2d, start = 0).diffs, start = 0).prefs)
    print('------')

    tensor2d_diff = Diffs2D(tensor2d)
    tensor2d_diff.add((0, 1), (2, 2), 100)
    print2d(Prefs2D(tensor2d_diff.diffs).prefs)
