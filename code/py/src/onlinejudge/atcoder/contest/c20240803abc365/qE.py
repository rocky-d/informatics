from itertools import accumulate
from operator import xor


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    prefs = list(accumulate(a, func = xor, initial = 0b0))
    print(sum(sum(prefs[i] ^ prefs[j] for j in range(i + 2, n + 1)) for i in range(0, n - 1)))


if __name__ == '__main__':
    main()
