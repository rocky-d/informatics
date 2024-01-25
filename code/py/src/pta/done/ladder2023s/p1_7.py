def main() -> None:
    n, m, q = map(int, input().split())
    t, c = [], []
    for _ in range(q):
        t_, c_ = input().split()
        t.append('0' == t_)
        c.append(int(c_))

    rows, cols = [True for _ in range(1 + n)], [True for _ in range(1 + m)]
    for i in range(q):
        if t[i]:
            rows[c[i]] = False
        else:
            cols[c[i]] = False
    ans = 0
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            if rows[i] and cols[j]:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
