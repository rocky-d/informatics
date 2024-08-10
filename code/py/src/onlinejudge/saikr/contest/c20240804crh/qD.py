def main() -> None:
    n = int(input())
    a = (int(input()) for _ in range(n))

    ans = 0
    a = list(a)
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
            else:
                break
        ans += cnt
    print(ans)


if __name__ == '__main__':
    main()
