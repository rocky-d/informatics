from collections import Counter


def main() -> None:
    n, m = map(int, input().split())

    length = n
    cnter = Counter()
    row = Counter()
    row[1] = n
    cnter[1] = n
    num1, num2 = 1, 1
    while 1 < length:
        row_nxt = Counter()
        mod = length % 4
        if 0 == mod:
            length //= 2
            num1 <<= 1
            row_nxt[num1] = length
            num2 = num1
        elif 1 == mod:
            length = 1 + length // 2
            num1 <<= 1
            row_nxt[num1] = length - 1
            row_nxt[num2] = 1
        elif 2 == mod:
            length //= 2
            num1 <<= 1
            row_nxt[num1] = length
            num2 = num1
        else:  # 3 == mod:
            length = length // 2
            num2 += num1 + num1
            num1 <<= 1
            row_nxt[num1] = length - 1
            row_nxt[num2] = 1
        for key, val in row_nxt.items():
            cnter[key] += val
    ans = []
    for q in map(int, input().split()):
        ans.append(cnter[q])
    print(*ans)


if __name__ == '__main__':
    main()
