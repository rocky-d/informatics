from collections import Counter


def main() -> None:
    n = int(input())
    s = input()

    ans = 0
    cnter = Counter(s)
    del cnter['?']
    for key, cnt in cnter.items():
        ans += min(n, cnt)
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
