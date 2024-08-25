def main() -> None:
    n = int(input())
    s = input()
    uv = (map(int, input().split()) for _ in range(n - 1))

    ans = 0
    s = '_' + s
    for u, v in uv:
        if s[u] == s[v]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
