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
        self._list = list(zip((self._convert(item) for item in self._origin), range(len(self._origin))))
        heapify(self._list)

    def __len__(self):
        return len(self._list)

    def pop(self):
        _, index = heappop(self._list)
        item = self._origin[index]
        self._origin[index] = self._origin.pop(-1)
        for i in range(len(self._list)):
            if len(self._list) == self._list[i][1]:
                self._list[i] = self._list[i][0], index
                break
        return item

    def push(self, item):
        self._origin.append(item)
        heappush(self._list, (self._convert(item), len(self._list)))

    def pushpop(self, item):  # TODO
        return ...

    def replace(self, item):  # TODO
        return ...

    def peek(self):
        return self._origin[self._list[0][1]]

    def peekall(self):
        items = []
        list_ = self._list.copy()
        for _ in range(len(list_)):
            items.append(self._origin[heappop(list_)[1]])
        return items

    def peekn(self, n):
        items = []
        list_ = self._list.copy()
        for _ in range(min(n, len(list_))):
            items.append(self._origin[heappop(list_)[1]])
        return items

    # def peekn(self, n):
    #     items = []
    #     pops = []
    #     for _ in range(min(n, len(self._list))):
    #         pops.append(heappop(self._list))
    #         items.append(self._origin[pops[-1][1]])
    #     for _ in range(len(pops)):
    #         heappush(self._list, pops.pop(-1))
    #     return items


if __name__ == '__main__':
    heap = Heap([9, 13, 8, 1, 2, 3, 4, 5], reverse = True)
    print(heap.peekall())
    heap.push(7)
    print(heap.peekall())
