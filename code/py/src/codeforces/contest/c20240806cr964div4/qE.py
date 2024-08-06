from functools import lru_cache
from math import log


@lru_cache(maxsize = None)
def func(num: int) -> int:
    return 1 + int(log(num, 3))


def main() -> None:
    l, r = map(int, input().split())

    print(func(l) + sum(func(num) for num in range(l, r + 1)))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
