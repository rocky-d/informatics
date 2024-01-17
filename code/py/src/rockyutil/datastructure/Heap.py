from heapq import heapify, heappop, heappush, heappushpop, heapreplace


class Heap(object):

    @staticmethod
    def _converse(item):
        return -item

    def __init__(self, __iterable, *, key = None, reverse = False):
        self._key = key
        self._reverse = reverse
        self._origin = list(__iterable)
        if self._key is None:
            if not self._reverse:
                self._convert = lambda item_: item_
            else:
                self._convert = lambda item_: Heap._converse(item_)
        else:
            if not self._reverse:
                self._convert = lambda item_: self._key(item_)
            else:
                self._convert = lambda item_: Heap._converse(self._key(item_))
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

    def replace(self, item):
        return heapreplace(self._heap, item)

    def pushpop(self, item):
        return heappushpop(self._heap, item)

    def peek(self, n = 1):
        return ...


if __name__ == '__main__':
    heap = Heap([1, 2, 3, 4, 5], key = lambda x: x - 10, reverse = True)
    print(heap._heap)
    heap.push(4)
    print(heap._heap)

    print(heap.pop())
