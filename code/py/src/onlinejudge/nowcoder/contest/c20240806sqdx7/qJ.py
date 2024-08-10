def main() -> None:
    l, x, y = map(int, input().split())

    l2, x2, y2 = l * l, x * x, y * y
    if x2 + y2 <= l2:
        print('Yes')
        print(0)
    elif (l - x) ** 2 + y2 <= l2:
        print('Yes')
        print(l)
    else:
        print('No')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
