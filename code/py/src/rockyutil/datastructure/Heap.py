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
        self._heap = list(zip((self._convert(item) for item in self._origin), range(len(self._origin))))
        heapify(self._heap)

    def __len__(self):
        return len(self._heap)

    def pop(self):
        _, index = heappop(self._heap)
        item = self._origin[index]
        self._origin[index] = self._origin.pop(-1)
        for i in range(len(self._heap)):
            if len(self._heap) == self._heap[i][1]:
                self._heap[i] = self._heap[i][0], index
                break
        return item

    def push(self, item):
        self._origin.append(item)
        heappush(self._heap, (self._convert(item), len(self._heap)))

    def pushpop(self, item):  # TODO
        return heappushpop(self._heap, item)

    def replace(self, item):  # TODO
        return heapreplace(self._heap, item)

    def peek(self):
        return self._origin[self._heap[0][1]]

    # def peekn(self, n):
    #     items = []
    #     pops = []
    #     for _ in range(min(n, len(self._heap))):
    #         pops.append(heappop(self._heap))
    #         items.append(self._origin[pops[-1][1]])
    #     for _ in range(len(pops)):
    #         heappush(self._heap, pops.pop(-1))
    #     return items

    def peekn(self, n):
        items = []
        heap_ = self._heap.copy()
        for _ in range(min(n, len(heap_))):
            items.append(self._origin[heappop(heap_)[1]])
        return items

    def peekall(self):
        items = []
        heap_ = self._heap.copy()
        for _ in range(len(heap_)):
            items.append(self._origin[heappop(heap_)[1]])
        return items


if __name__ == '__main__':
    heap = Heap([9, 13, 8, 1, 2, 3, 4, 5], reverse = True)
    print(heap.peekall())
    heap.push(7)
    print(heap.peekall())
