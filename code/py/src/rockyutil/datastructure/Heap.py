from heapq import heapify, heappop, heappush, heappushpop, heapreplace


class Heap(object):

    @staticmethod
    def _converse(item):
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

    def push(self, item):
        self._origin.append(item)
        heappush(self._heap, (self._convert(item), len(self._heap)))

    def pop(self):
        _, index = heappop(self._heap)
        item = self._origin[index]
        self._origin[index] = self._origin.pop(-1)
        for i in range(len(self._heap)):
            if len(self._heap) == self._heap[i][1]:
                self._heap[i] = self._heap[i][0], index
                break
        return item

    def replace(self, item):  # TODO
        return heapreplace(self._heap, item)

    def pushpop(self, item):  # TODO
        return heappushpop(self._heap, item)

    def peek(self):
        return self._origin[self._heap[0][1]]

    # def peekn(self, n):
    #     items = []
    #     pops = []
    #     for _ in range(min(n, len(self._heap))):
    #         pops.append(heappop(self._heap))
    #         items.append(self._origin[pops[-1][1]])
    #     while 0 < len(pops):
    #         heappush(self._heap, pops.pop(-1))
    #     return items

    def peekn(self, n):
        items = []
        heap = self._heap.copy()
        for _ in range(min(n, len(heap))):
            items.append(self._origin[heappop(heap)[1]])
        return items


if __name__ == '__main__':
    h = Heap([1, 2, 3, 4, 5], key = lambda x: x - 10, reverse = True)
    print(h._heap)
    h.push(4)
    print(h._heap)
    print(h.pop())
