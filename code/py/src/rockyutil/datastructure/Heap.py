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
            # self._heap = list(zip((Heap._converse(item) for item in self._origin) if self._reverse else (item for item in self._origin), range(len(self._origin))))
            if not self._reverse:
                self._heap = list(zip((item for item in self._origin), range(len(self._origin))))
            else:
                self._heap = list(zip((Heap._converse(item) for item in self._origin), range(len(self._origin))))
        else:
            # self._heap = list(zip((Heap._converse(self._key(item)) for item in self._origin) if self._reverse else (self._key(item) for item in self._origin), range(len(self._origin))))
            if not self._reverse:
                self._heap = list(zip((self._key(item) for item in self._origin), range(len(self._origin))))
            else:
                self._heap = list(zip((Heap._converse(self._key(item)) for item in self._origin), range(len(self._origin))))
        heapify(self._heap)

    def push(self, item):
        heappush(self._heap, item)

    def pop(self):
        return heappop(self._heap)

    def replace(self, item):
        return heapreplace(self._heap, item)

    def pushpop(self, item):
        return heappushpop(self._heap, item)

    def peek(self, n = 1):
        return ...


if __name__ == '__main__':
    ...
