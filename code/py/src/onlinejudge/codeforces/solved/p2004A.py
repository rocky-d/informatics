def main() -> None:
    n = int(input())
    x = map(int, input().split())

    x = list(x)
    print('YES' if 2 == n and 1 < abs(x[0] - x[1]) else 'NO')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
