from bisect import bisect_left


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0

    def check(mid):
        ...
        return False

    bisect_left(range(1_000_000_001), k, lo = 0, key = check)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
