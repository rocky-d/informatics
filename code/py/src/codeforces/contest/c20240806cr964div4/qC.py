def main() -> None:
    n, s, m = map(int, input().split())
    lr = (map(int, input().split()) for _ in range(n))

    lr = list(lr)
    time = 0
    for l, r in lr:
        if s <= l - time:
            ans = 'YES'
            break
        time = r
    else:
        ans = 'YES' if s <= m - time else 'NO'
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
