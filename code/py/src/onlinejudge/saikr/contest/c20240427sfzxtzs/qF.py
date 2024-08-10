def main() -> None:
    n, na, nb = map(int, input().split())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))

    cnt_a, cnt_b = 0, 0
    rules = (
        (0, -1, 1, 1, -1),
        (1, 0, -1, 1, -1),
        (-1, 1, 0, -1, 1),
        (-1, -1, 1, 0, 1),
        (1, 1, -1, -1, 0),
    )
    ai, bi = 0, 0
    for _ in range(n):
        res = rules[a[ai]][b[bi]]
        if -1 == res:
            cnt_b += 1
        elif 1 == res:
            cnt_a += 1
        ai = (ai + 1) % na
        bi = (bi + 1) % nb
    print(cnt_a, cnt_b)


if __name__ == '__main__':
    main()
