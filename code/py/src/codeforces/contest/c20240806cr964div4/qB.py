def main() -> None:
    a1, a2, b1, b2 = map(int, input().split())

    ans = 0
    cnt = 0
    if a1 > b1:
        cnt += 1
    elif a1 < b1:
        cnt -= 1
    if a2 > b2:
        cnt += 1
    elif a2 < b2:
        cnt -= 1
    if 0 < cnt:
        ans += 2
    cnt = 0
    if a1 > b2:
        cnt += 1
    elif a1 < b2:
        cnt -= 1
    if a2 > b1:
        cnt += 1
    elif a2 < b1:
        cnt -= 1
    if 0 < cnt:
        ans += 2
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
