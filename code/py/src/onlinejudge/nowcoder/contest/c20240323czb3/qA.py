def main() -> None:
    n = int(input())
    a = map(int, input().split())

    ans = 0
    for ai in a:
        if 1 != ai:
            ans += ai
    print(ans)


if __name__ == '__main__':
    main()
