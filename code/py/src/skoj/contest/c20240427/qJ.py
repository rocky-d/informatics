from collections import Counter
from heapq import *


def main() -> None:
    for _ in range(int(input())):
        n = int(input())
        s = input()
        heap = list(map(lambda x: -x, Counter(s).values()))
        heapify(heap)
        while 2 <= len(heap):
            x, y = -heappop(heap), -heappop(heap)
            x -= 1
            y -= 1
            if 0 < x:
                heappush(heap, -x)
            if 0 < y:
                heappush(heap, -y)
        print(-sum(heap))


if __name__ == '__main__':
    main()
