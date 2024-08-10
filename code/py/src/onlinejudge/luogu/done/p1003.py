def main() -> None:
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    table = [None] + table
    x, y = map(int, input().split())
    res = -1
    for i in range(n, 0, -1):
        if table[i][0] <= x <= table[i][0] + table[i][2] and table[i][1] <= y <= table[i][1] + table[i][3]:
            res = i
            break
    print(res)


if __name__ == '__main__':
    main()
