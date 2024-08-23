def main() -> None:
    n = int(input())

    ans = 0
    while 0 < n:
        n = n % (n // 2 + 1)
        ans += 1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
