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
        self._prefs = [self._start]
        for i, x in enumerate(__tensor1d, 1):
            self._prefs.append(x + self._prefs[i - 1])

    def sum(self, lo, hi):  # [lo, hi]
        hi = hi + 1
        return self._prefs[hi] - self._prefs[lo]


class Diffs1D(_Diffs):

    def __init__(self, __tensor1d, start = 0):
        super().__init__(start)
        self._diffs = [__tensor1d[0] - self._start]
        for lst, nxt in pairwise(__tensor1d):
            self._diffs.append(nxt - lst)

    def add(self, lo, hi, val):  # [lo, hi]
        self._diffs[lo] += val
        hi = hi + 1
        if hi != len(self._diffs):
            self._diffs[hi] -= val


class Prefs2D(_Prefs):

    def __init__(self, __tensor2d, start = 0):
        super().__init__(start)
        self._prefs = [[self._start] + [self._start for _ in __tensor2d[0]]] + [[self._start] for _ in __tensor2d]
        for i, x1d in enumerate(__tensor2d, 1):
            for j, x in enumerate(x1d, 1):
                self._prefs[i].append(x - self._prefs[i - 1][j - 1] + self._prefs[i - 1][j] + self._prefs[i][j - 1])

    def sum(self, lo, hi):  # [lo, hi]
        hi = hi[0] + 1, hi[1] + 1
        return self._prefs[hi[0]][hi[1]] + self._prefs[lo[0]][lo[1]] - self._prefs[lo[0]][hi[1]] - self._prefs[hi[0]][lo[1]]


class Diffs2D(_Diffs):

    def __init__(self, __tensor2d, start = 0):
        super().__init__(start)
        self._diffs = [[__tensor2d[0][0] - self._start]]
        for lst, nxt in pairwise(__tensor2d[0]):
            self._diffs[0].append(nxt - lst)
        for lst1d, nxt1d in pairwise(__tensor2d):
            self._diffs.append([nxt1d[0] - lst1d[0]])
            for (lst_lst, lst_nxt), (nxt_lst, nxt_nxt) in zip(pairwise(lst1d), pairwise(nxt1d)):
                self._diffs[-1].append(nxt_nxt + lst_lst - lst_nxt - nxt_lst)

    def add(self, lo, hi, val):  # [lo, hi]
        self._diffs[lo[0]][lo[1]] += val
        hi = hi[0] + 1, hi[1] + 1
        if hi[0] != len(self._diffs) and hi[1] != len(self._diffs[0]):
            self._diffs[hi[0]][hi[1]] += val
        if hi[0] != len(self._diffs):
            self._diffs[hi[0]][lo[1]] -= val
        if hi[1] != len(self._diffs):
            self._diffs[lo[0]][hi[1]] -= val


if __name__ == '__main__':
    print_ = lambda __iterable: print(*__iterable, sep = '\n', end = '\n\n')

    tensor_1d = [1, 2, 3, 4, 5]
    print(tensor_1d)
    print(Prefs1D(tensor_1d, start = 0).prefs)
    print(Diffs1D(tensor_1d, start = 0).diffs)
    print(Diffs1D(Prefs1D(tensor_1d, start = 0).prefs, start = 0).diffs)
    print(Prefs1D(Diffs1D(tensor_1d, start = 0).diffs, start = 0).prefs)
    print('------')

    tensor_2d = [
        [1, 2, 3],
        [5, 5, 3],
        [8, 2, 4],
    ]
    print_(tensor_2d)
    print_(Prefs2D(tensor_2d, start = 0).prefs)
    print_(Diffs2D(tensor_2d, start = 0).diffs)
    print_(Diffs2D(Prefs2D(tensor_2d, start = 0).prefs, start = 0).diffs)
    print_(Prefs2D(Diffs2D(tensor_2d, start = 0).diffs, start = 0).prefs)
    print('------')

    tensor_2d_diff = Diffs2D(tensor_2d)
    tensor_2d_diff.add((0, 1), (2, 2), 100)
    print_(Prefs2D(tensor_2d_diff.diffs).prefs)
