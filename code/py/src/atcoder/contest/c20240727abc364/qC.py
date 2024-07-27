from itertools import accumulate


def main() -> None:
    n, x, y = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = n
    for i, pref in enumerate(accumulate(sorted(a, reverse = True)), start = 1):
        if x < pref:
            ans = min(ans, i)
            break
    for i, pref in enumerate(accumulate(sorted(b, reverse = True)), start = 1):
        if y < pref:
            ans = min(ans, i)
            break
    print(ans)


if __name__ == '__main__':
    main()
