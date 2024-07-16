def main() -> None:
    q = int(input())
    ax = (map(int, input().split()) for _ in range(q))

    ans = []
    for a, x in ax:
        ans.append((a if 1 == x else a * a * x * (x - 1) // 2) % 998244353)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
