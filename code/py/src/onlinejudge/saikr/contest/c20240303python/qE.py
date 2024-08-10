from collections import Counter
from heapq import *


def case() -> None:
    n = int(input().strip())
    s = input().strip()

    nums = list(map(lambda x: -x, Counter(s).values()))
    heapify(nums)
    while 2 <= len(nums):
        a, b = -heappop(nums), -heappop(nums)
        a -= 1
        b -= 1
        if 0 < a:
            heappush(nums, -a)
        if 0 < b:
            heappush(nums, -b)
    print(-sum(nums))


def main() -> None:
    for _ in range(int(input().strip())):
        case()


if __name__ == '__main__':
    main()
