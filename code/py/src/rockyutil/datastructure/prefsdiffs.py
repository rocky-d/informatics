from itertools import pairwise


class _Prefs(object):

    def __init__(self, __start):
        self._start = __start
        self._prefs = None

    @property
    def start(self):
        return self._start

    @property
    def prefs(self):
        return self._prefs


class _Diffs(object):

    def __init__(self, __start):
        self._start = __start
        self._diffs = None

    @property
    def start(self):
        return self._start

    @property
    def diffs(self):
        return self._diffs


class Prefs1D(_Prefs):

    def __init__(self, tensor1d, start = 0):
        super().__init__(start)
        self._prefs = [self._start]
        for i, x in enumerate(tensor1d, 1):
            self._prefs.append(x + self._prefs[i - 1])


class Diffs1D(_Diffs):

    def __init__(self, tensor1d, start = 0):
        super().__init__(start)
        self._diffs = [tensor1d[0] - self._start]
        for lst, nxt in pairwise(tensor1d):
            self._diffs.append(nxt - lst)


class Prefs2D(_Prefs):

    def __init__(self, tensor2d, start = 0):
        super().__init__(start)
        self._prefs = [[self._start] + [self._start for _ in tensor2d[0]]] + [[self._start] for _ in tensor2d]
        for i, x1d in enumerate(tensor2d, 1):
            for j, x in enumerate(x1d, 1):
                self._prefs[i].append(x - self._prefs[i - 1][j - 1] + self._prefs[i - 1][j] + self._prefs[i][j - 1])


class Diffs2D(_Diffs):

    def __init__(self, tensor2d, start = 0):
        super().__init__(start)
        self._diffs = [[tensor2d[0][0] - self._start]]
        for lst, nxt in pairwise(tensor2d[0]):
            self._diffs[0].append(nxt - lst)
        for lst1d, nxt1d in pairwise(tensor2d):
            self._diffs.append([nxt1d[0] - lst1d[0]])
            for (lst_lst, lst_nxt), (nxt_lst, nxt_nxt) in zip(pairwise(lst1d), pairwise(nxt1d)):
                self._diffs[-1].append(nxt_nxt + lst_lst - lst_nxt - nxt_lst)


if __name__ == '__main__':
    tensor_1d = [1, 2, 3, 4, 5]
    print(tensor_1d)
    print(Prefs1D(tensor_1d, 0).prefs)
    print(Diffs1D(tensor_1d, 0).diffs)
    print(Diffs1D(Prefs1D(tensor_1d, 0).prefs, 0).diffs)
    print(Prefs1D(Diffs1D(tensor_1d, 0).diffs, 0).prefs)
    print('------')

    tensor_2d = [
        [1, 2, 3],
        [5, 5, 3],
        [8, 2, 4],
    ]
    print(*tensor_2d, sep = '\n', end = '\n\n')
    print(*Prefs2D(tensor_2d, 0).prefs, sep = '\n', end = '\n\n')
    print(*Diffs2D(tensor_2d, 0).diffs, sep = '\n', end = '\n\n')
    print(*Diffs2D(Prefs2D(tensor_2d, 0).prefs, 0).diffs, sep = '\n', end = '\n\n')
    print(*Prefs2D(Diffs2D(tensor_2d, 0).diffs, 0).prefs, sep = '\n', end = '\n\n')
    print('------')
