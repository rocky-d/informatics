from collections import Counter


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    print(n - max(Counter(a).values()))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
