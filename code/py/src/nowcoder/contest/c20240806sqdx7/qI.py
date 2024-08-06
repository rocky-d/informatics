from bisect import bisect_left


def main() -> None:
    m, k, h = map(int, input().split())

    if m <= k:
        print(min(h, m))
        return
    diff = m - k
    print(bisect_left(range(h + 1), h, lo = 0, key = lambda mid: mid + k * max(0, 1 + (mid - m) // diff)))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
