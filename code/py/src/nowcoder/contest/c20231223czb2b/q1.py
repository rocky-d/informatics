def main() -> None:
    n, a = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if x[i] >= a > x[i - 1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
