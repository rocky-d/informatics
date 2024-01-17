from heapq import heappush, heappop, heapreplace, heappushpop, heapify


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
                heap_items = (item for item in self._origin)
            else:
                heap_items = (Heap._converse(item) for item in self._origin)
        else:
            if not self._reverse:
                heap_items = (self._key(item) for item in self._origin)
            else:
                heap_items = (Heap._converse(self._key(item)) for item in self._origin)
        self._heap = list(zip(heap_items, range(len(self._origin))))
        heapify(self._heap)

    def push(self, item):
        self._origin.append(item)
        if self._key is None:
            if not self._reverse:
                heap_item = item
            else:
                heap_item = Heap._converse(item)
        else:
            if not self._reverse:
                heap_item = self._key(item)
            else:
                heap_item = Heap._converse(self._key(item))
        heappush(self._heap, (heap_item, len(self._heap)))

    def pop(self):
        _, index = heappop(self._heap)
        item = self._origin[index]
        self._origin[index] = self._origin.pop(-1)
        for heap_item, i in self._heap:
            if i == len(self._heap):
                self._heap[i] = heap_item, index
        return item

    def replace(self, item):
        return heapreplace(self._heap, item)

    def pushpop(self, item):
        return heappushpop(self._heap, item)

    def peek(self, n = 1):
        return ...


if __name__ == '__main__':
    heap = Heap([1, 2, 3, 4, 5], key = lambda x: -x)
    print(heap._heap)
    heap.push(4)
    print(heap._heap)
