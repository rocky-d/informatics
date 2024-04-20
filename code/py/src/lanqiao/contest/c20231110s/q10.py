def main() -> None:
    n = int(input())
    a = [-1] + list(map(int, input().split()))
    k = int(input())
    ans = ''
    for i in range(1, n + 1):
        ans += str(min(a[max(1, i - k):1 + min(n, i + k)])) + ' '
    print(ans)


if __name__ == '__main__':
    main()
