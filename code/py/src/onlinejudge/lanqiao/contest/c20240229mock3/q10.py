def main() -> None:
    n = int(input())
    a, b, c = map(int, input().split())

    dp, dp_len = [0, 0, 1], 3
    for _ in range(1, 1 + n):
        dp.append(dp[-min(a, dp_len)] + dp[-min(b, dp_len)] + dp[-min(c, dp_len)])
        dp_len += 1
    print(dp[-1])


if __name__ == '__main__':
    main()
