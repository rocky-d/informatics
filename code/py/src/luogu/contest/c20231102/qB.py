def main() -> None:
    input()
    x_ls = list(map(int, input().split()))
    y_ls = list(map(int, input().split()))

    dp = [[0, 0, 0] for _i in range(3)]

    for x, y in zip(x_ls, y_ls):
        for j in range(3, 0, -1):
            if dp[j][0] <= x:
                if 1 == y:
                    ...


if __name__ == '__main__':
    main()
