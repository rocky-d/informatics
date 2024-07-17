def main() -> None:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = map(int, input().split())
        b = map(int, input().split())
        res = 0
        pref_a = 0
        max_b = 0
        for i in range(1, min(n, k) + 1):
            pref_a += next(a)
            max_b = max(max_b, next(b))
            res = max(res, pref_a + (k - i) * max_b)
        print(res)


if __name__ == '__main__':
    main()
