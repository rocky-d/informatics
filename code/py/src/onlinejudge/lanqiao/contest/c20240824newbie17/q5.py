def main() -> None:
    n = int(input())
    b = map(int, input().split())

    print('YES' if min(b) <= 1 else 'NO')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
