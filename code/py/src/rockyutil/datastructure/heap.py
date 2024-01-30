from heapq import heapify, heappop, heappush, heappushpop, heapreplace


class Heap(object):

    @staticmethod
    def _converse(item):  # TODO
        return -item

    def __init__(self, __iterable, *, key = None, reverse = False):
        self._origin = list(__iterable)
        if key is None:
            if not reverse:
                self._convert = lambda item_: item_
            else:
                self._convert = lambda item_: Heap._converse(item_)
        else:
            if not reverse:
                self._convert = lambda item_: key(item_)
            else:
                self._convert = lambda item_: Heap._converse(key(item_))
        self._table = list(zip((self._convert(item) for item in self._origin), range(len(self._origin))))
        heapify(self._table)

    def __len__(self):
        return len(self._table)

    def pop(self):
        _, index = heappop(self._table)
        item = self._origin[index]
        self._origin[index] = self._origin.pop(-1)
        for i in range(len(self._table)):
            if len(self._table) == self._table[i][1]:
                self._table[i] = self._table[i][0], index
                break
        return item

    def push(self, item):
        self._origin.append(item)
        heappush(self._table, (self._convert(item), len(self._table)))

    def pushpop(self, item):  # TODO
        return ...

    def replace(self, item):  # TODO
        return ...

    def peek(self):
        return self._origin[self._table[0][1]]

    def peekall(self):
        items = []
        table_ = self._table.copy()
        for _ in range(len(table_)):
            items.append(self._origin[heappop(table_)[1]])
        return items

    def peekn(self, n):
        items = []
        table_ = self._table.copy()
        for _ in range(min(n, len(table_))):
            items.append(self._origin[heappop(table_)[1]])
        return items

    # def peekn(self, n):
    #     items = []
    #     pops = []
    #     for _ in range(min(n, len(self._table))):
    #         pops.append(heappop(self._table))
    #         items.append(self._origin[pops[-1][1]])
    #     for _ in range(len(pops)):
    #         heappush(self._table, pops.pop(-1))
    #     return items


if __name__ == '__main__':
    heap = Heap([9, 13, 8, 1, 2, 3, 4, 5], reverse = True)
    print(heap.peekall())
    heap.push(7)
    print(heap.peekall())
