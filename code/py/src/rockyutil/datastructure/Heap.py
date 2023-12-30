from _typeshed import SupportsRichComparison
from heapq import heappush, heappop, heapreplace, heappushpop
from typing import Callable, TypeVar, Iterable

_T = TypeVar('_T')


class Heap(object):

    def __init__(
            self,
            iterable: Iterable[_T],
            *,
            key: Callable[[_T], SupportsRichComparison] | None = None,
            reverse: bool = False
    ) -> None:
        self._heap: list = list()
        if key is None:
            if not reverse:
                ...
            else:
                ...
        else:
            if not reverse:
                ...
            else:
                ...

    def push(self, item: _T) -> None:
        heappush(self._heap, item)

    def pop(self) -> _T:
        return heappop(self._heap)

    def replace(self, item: _T) -> _T:
        return heapreplace(self._heap, item)

    def pushpop(self, item: _T) -> _T:
        return heappushpop(self._heap, item)

    def peek(self, n: int = 1) -> list[_T]:
        ...


if __name__ == '__main__':
    ...
