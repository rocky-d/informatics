def main() -> None:
    n = int(input())
    a = map(int, input().split())

    print(10 + sum(ai * ai + 4 * ai for ai in a))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
