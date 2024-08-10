from itertools import groupby


def main() -> None:
    n = int(input())
    s = input()
    x, y, z = map(int, input().split())

    ans = 0
    zeros = 0
    for char, ls in groupby(s):
        cnt = len(list(ls))
        if '0' == char:
            zeros += cnt
        else:  # elif '1' == char:
            ans += min(zeros, cnt)
            zeros = max(0, zeros - cnt)
            if y <= ans:
                break
    print(min(y, ans))


if __name__ == '__main__':
    main()
