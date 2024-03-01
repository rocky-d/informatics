from itertools import pairwise


class _Prefs(object):

    def __init__(self):
        self._prefs = None

    @property
    def prefs(self):
        return self._prefs


class _Diffs(object):

    def __init__(self):
        self._diffs = None

    @property
    def diffs(self):
        return self._diffs


class Prefs1D(_Prefs):

    def __init__(self, tensor1, start = 0):
        super().__init__()
        self._prefs = [start]
        for i, x in enumerate(tensor1, 1):
            self._prefs.append(x + self._prefs[i - 1])


class Diffs1D(_Diffs):

    def __init__(self, tensor1, start = 0):
        super().__init__()
        self._diffs = [tensor1[0] - start]
        for lst, nxt in pairwise(tensor1):
            self._diffs.append(nxt - lst)


class Prefs2D(_Prefs):

    def __init__(self, tensor2, start = 0):
        super().__init__()
        self._prefs = [[start] + [start for _ in tensor2[0]]] + [[start] for _ in tensor2]
        for i, x1 in enumerate(tensor2, 1):
            for j, x in enumerate(x1, 1):
                self._prefs[i].append(x - self._prefs[i - 1][j - 1] + self._prefs[i - 1][j] + self._prefs[i][j - 1])


class Diffs2D(_Diffs):

    def __init__(self, tensor2, start = 0):
        super().__init__()
        self._diffs = [[tensor2[0][0] - start]]
        for lst, nxt in pairwise(tensor2[0]):
            self._diffs[0].append(nxt - lst)
        for lst1, nxt1 in pairwise(tensor2):
            self._diffs.append([nxt1[0] - lst1[0]])
            for (lst_lst, lst_nxt), (nxt_lst, nxt_nxt) in zip(pairwise(lst1), pairwise(nxt1)):
                self._diffs[-1].append(nxt_nxt + lst_lst - lst_nxt - nxt_lst)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(Prefs1D(nums).prefs)
    print(Diffs1D(nums).diffs)
    print(Diffs1D(Prefs1D(nums).prefs).diffs)
    print(Prefs1D(Diffs1D(nums).diffs).prefs)
    print('------')

    matrix = [
        [1, 2, 3],
        [5, 5, 3],
        [8, 2, 4],
    ]
    print(*Prefs2D(matrix).prefs, sep = '\n', end = '\n\n')
    print(*Diffs2D(matrix).diffs, sep = '\n', end = '\n\n')
    print(*Diffs2D(Prefs2D(matrix).prefs).diffs, sep = '\n', end = '\n\n')
    print(*Prefs2D(Diffs2D(matrix).diffs).prefs, sep = '\n', end = '\n\n')
    print('------')
