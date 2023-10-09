def main() -> None:
    WIN_TABLE = ((0, -1, 1, 1, -1),
                 (1, 0, -1, 1, -1),
                 (-1, 1, 0, -1, 1),
                 (-1, -1, 1, 0, 1),
                 (1, 1, -1, -1, 0))
    n, na, nb = map(int, input().split())
    a_ls = list(map(int, input().split()))
    b_ls = list(map(int, input().split()))
    ans = [0, 0]
    a_index, b_index = 0, 0
    for _ in range(n):
        res = WIN_TABLE[a_ls[a_index]][b_ls[b_index]]
        if 1 == res:
            ans[0] += 1
        elif -1 == res:
            ans[1] += 1
        a_index, b_index = (a_index + 1) % na, (b_index + 1) % nb
    print(*ans)


if __name__ == '__main__':
    main()
