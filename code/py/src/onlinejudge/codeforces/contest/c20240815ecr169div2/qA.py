def main() -> None:
    n = int(input())
    x = map(int, input().split())

    x = sorted(x)
    if 2 == n:
        print('YES' if 1 < x[1] - x[0] else 'NO')
    else:
        print('NO')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
