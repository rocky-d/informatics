from functools import lru_cache


@lru_cache(maxsize = None)
def func(num: int) -> int:
    res = 0
    while 0 < num:
        num //= 3
        res += 1
    return res


def main() -> None:
    l, r = map(int, input().split())

    print(func(l) + sum(func(num) for num in range(l, r + 1)))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
