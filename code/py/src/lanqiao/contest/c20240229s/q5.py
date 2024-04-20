from math import inf


def main() -> None:
    n, m = 30, 20
    side = 5
    matrix = (map(int, input().split()) for _ in range(n))

    ans = -inf
    pres = [[0] for _ in range(n)]
    for i, row in enumerate(matrix):
        pres_i = pres[i]
        for num in row:
            pres_i.append(pres_i[-1] + num)
    for i in range(n - side + 1):
        for j in range(m - side + 1):
            ans = max(ans, sum(pres[row][j + side] - pres[row][j] for row in range(i, i + side)))
    print(ans)


if __name__ == '__main__':
    main()
