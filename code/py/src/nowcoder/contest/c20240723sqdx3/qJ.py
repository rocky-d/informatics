def main() -> None:
    n, a, b = map(int, input().split())
    t = input()

    ans = ''
    # zeros = t.count('0')
    # ones = n - zeros
    for i in range(n):
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        idx = i
        while True:
            if '1' == t[idx]:
                x2 += 1
                if a == x2:
                    x2, y2 = 0, 0
                    x1 += 1
                    if b == x1:
                        ans += '1'
                        break
            else:
                y2 += 1
                if a == y2:
                    x2, y2 = 0, 0
                    y1 += 1
                    if b == y1:
                        ans += '0'
                        break
            idx += 1
            idx %= n
    print(ans)


if __name__ == '__main__':
    main()
