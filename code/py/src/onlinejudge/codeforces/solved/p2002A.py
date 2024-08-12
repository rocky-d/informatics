def main() -> None:
    n, m, k = map(int, input().split())

    print(min(k, n) * min(k, m))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
