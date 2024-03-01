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

    def __init__(self, __iterable, start = 0):
        super().__init__()
        self._pres = [start]
        for i, x in enumerate(__iterable, 1):
            self._pres.append(x + self._pres[i - 1])


class Diffs1D(_Diffs):

    def __init__(self, __iterable, start = 0):
        super().__init__()
        self._diffs = []
        lst_x = start
        for x in __iterable:
            self._diffs.append(x - lst_x)
            lst_x = x


class Pres2D(_Pres):

    def __init__(self, __iterable, start = 0):
        super().__init__()
        self._pres = [[start] + [start for _ in __iterable[0]]] + [[start] for _ in __iterable]
        for i, row in enumerate(__iterable, 1):
            for j, x in enumerate(row, 1):
                self._pres[i].append(x - self._pres[i - 1][j - 1] + self._pres[i - 1][j] + self._pres[i][j - 1])


class Diffs2D(_Diffs):

    def __init__(self, __iterable, start = 0):
        super().__init__()
        self._diffs = []
        lst_row = [start] + [start for _ in __iterable]
        for row in __iterable:
            self._diffs.append([])
            lst_x = start
            for x in row:
                self._diffs[-1].append(x + lst_row.pop(0) - lst_row[0] - lst_x)
                lst_x = x
            lst_row = [start] + [x for x in row]


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
