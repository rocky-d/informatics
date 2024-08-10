def main() -> None:
    xc, yc, k = map(int, input().split())

    ans = []
    if 0b1 == 0b1 & k:
        ans.append(f"{xc} {yc}")
    for i in range(1, 1 + (k >> 1)):
        ans.append(f"{xc - i} {yc - i}")
        ans.append(f"{xc + i} {yc + i}")
    print(*ans, sep = '\n')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
