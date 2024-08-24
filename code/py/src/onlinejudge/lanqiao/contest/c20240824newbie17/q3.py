from collections import Counter


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    cnter = sorted(Counter(a).values(), reverse=True)
    if k <= len(cnter):
        print(k)
        return
    ans = len(cnter)
    k -= ans
    for cnt in cnter:
        ans -= 1
        k -= min(k, cnt - 1)
        if 0 == k:
            break
    print(ans)


if __name__ == '__main__':
    main()
