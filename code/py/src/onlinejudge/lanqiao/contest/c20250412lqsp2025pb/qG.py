def main():
    n = int(input())
    a = map(int, input().split())

    ans = 0
    a = [0] + list(a)
    unsorted = set()
    for i, ai in enumerate(a):
        if i != ai:
            unsorted.add(i)
    flips = 0
    for i in unsorted:
        if i == a[a[i]]:
            flips += 1
    ans += flips // 2
    ans += max(0, len(unsorted) - flips - 1)
    print(ans)


main()
