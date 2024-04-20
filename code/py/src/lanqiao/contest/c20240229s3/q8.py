def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    ans = [-1, 10_001]
    for i in range(1, n - 1):
        ai = a[i]
        if ai < a[i - 1] and ai < a[i + 1]:
            ans[0] = max(ans[0], ai)
        elif a[i - 1] < ai and a[i + 1] < ai:
            ans[1] = min(ans[1], ai)
    print(*ans)


if __name__ == '__main__':
    main()
