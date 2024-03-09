def main() -> None:
    w, p = map(int, input().split())

    ans = 0
    pct = 0.01 * (100 - p)
    v = 200_000 / w
    while 1e-6 < v:
        ans += v / 9.8
        v *= pct
    print(f"{ans:.3f}")


if __name__ == '__main__':
    main()
