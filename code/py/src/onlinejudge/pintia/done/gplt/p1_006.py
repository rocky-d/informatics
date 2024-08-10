from itertools import chain
from math import isqrt


def main():
    n = int(input())

    start, length = None, 0
    for i in chain(range(2, isqrt(n) + 1), [n]):
        cnt = 0
        num, factor = n, i
        while 0 == num % factor:
            num //= factor
            factor += 1
            cnt += 1
        if length < cnt:
            start, length = i, cnt
    print(length)
    print(*range(start, start + length), sep = '*')


if __name__ == "__main__":
    main()
