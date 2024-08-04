def main() -> None:
    n, x = map(eval, input().split())
    a = map(int, input().split())

    total = 0
    x /= 10
    x = 1 - x
    maxm = 0
    for ai in a:
        if ai > maxm:
            maxm = ai
        total += ai
    ans = int(100 * (total - x * maxm)) / 100
    print(f"{ans:.2f}")


if __name__ == '__main__':
    main()
