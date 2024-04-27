def main() -> None:
    a, b = map(int, input().split())
    print(str(pow(a, b))[-3:].zfill(3))


if __name__ == '__main__':
    main()
