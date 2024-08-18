def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a, reverse = True)
    for i in range(2, n):
        if a[i - 2] < a[i - 1] + a[i]:
            ans = a[i - 2] + a[i - 1] + a[i]
            break
    else:
        ans = -1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
