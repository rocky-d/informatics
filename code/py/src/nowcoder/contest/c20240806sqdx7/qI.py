from bisect import bisect_left


def main() -> None:
    m, k, h = map(int, input().split())

    if h <= m:
        print(h)
        return
    if m <= k:
        print(m)
        return
    diff = m - k
    print(bisect_left(range(h + 1), h, lo = m, key = lambda mid: mid + k * (1 + (mid - m) // diff)))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
