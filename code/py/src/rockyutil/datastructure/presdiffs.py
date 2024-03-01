from itertools import pairwise


class _Pres(object):

    def __init__(self):
        self._pres = None

    @property
    def pres(self):
        return self._pres


class _Diffs(object):

    def __init__(self):
        self._diffs = None

    @property
    def diffs(self):
        return self._diffs


class Pres1D(_Pres):

    def __init__(self, tensor, start = 0):
        super().__init__()
        self._pres = [start]
        for i, x in enumerate(tensor, 1):
            self._pres.append(x + self._pres[i - 1])


class Diffs1D(_Diffs):

    def __init__(self, tensor, start = 0):
        super().__init__()
        self._diffs = [tensor[0] - start]
        for lst, nxt in pairwise(tensor):
            self._diffs.append(nxt - lst)


class Pres2D(_Pres):

    def __init__(self, tensor, start = 0):
        super().__init__()
        self._pres = [[start] + [start for _ in tensor[0]]] + [[start] for _ in tensor]
        for i, row in enumerate(tensor, 1):
            for j, x in enumerate(row, 1):
                self._pres[i].append(x - self._pres[i - 1][j - 1] + self._pres[i - 1][j] + self._pres[i][j - 1])


class Diffs2D(_Diffs):

    def __init__(self, tensor, start = 0):
        super().__init__()
        self._diffs = [[tensor[0][0] - start]]
        for lst, nxt in pairwise(tensor[0]):
            self._diffs[0].append(nxt - lst)
        for lst1, nxt1 in pairwise(tensor):
            self._diffs.append([nxt1[0] - lst1[0]])
            for (lst_lst, lst_nxt), (nxt_lst, nxt_nxt) in zip(pairwise(lst1), pairwise(nxt1)):
                self._diffs[-1].append(nxt_nxt + lst_lst - lst_nxt - nxt_lst)


if __name__ == '__main__':
    nums = [1, 2, 5, 1]
    print(Pres1D(nums).pres)
    print(Diffs1D(nums).diffs)
    print()

    matrix = [
        [1, 2, 3],
        [5, 5, 3],
        [8, 2, 4],
    ]
    print(*Pres2D(matrix).pres, sep = '\n', end = '\n\n')
    print(*Diffs2D(matrix).diffs, sep = '\n', end = '\n\n')
    print(*Diffs2D(Pres2D(matrix).pres).diffs, sep = '\n', end = '\n\n')
    print(*Pres2D(Diffs2D(matrix).diffs).pres, sep = '\n', end = '\n\n')
    print()

    # matrix = [
    #     [100, 200, 300],
    #     [200, 301, 403],
    #     [300, 405, 512],
    # ]
    # print(*Diffs2D(matrix, 100).diffs, sep = '\n', end = '\n\n')
    # print()
