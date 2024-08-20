def main() -> None:
    n = int(input())

    if 0b0 == 0b1 & n:
        print(-1)
        return
    ans = []
    for i in range(1, n // 2 + 2):
        ans.append(i)
        ans.append(n + 1 - i)
    ans.pop(-1)
    print(*ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
