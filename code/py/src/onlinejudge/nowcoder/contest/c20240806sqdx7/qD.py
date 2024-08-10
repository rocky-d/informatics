from collections import Counter


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    ans = 0
    a = list(a)
    freq = Counter(a)
    for lft in range(n):
        maxm = n - lft
        cnter = Counter()
        for rit in range(lft, n):
            ai = a[rit]
            if freq[ai] < k:
                break
            cnter[ai] += 1
            if k < cnter[ai]:
                break
            length = k * len(cnter)
            if maxm < length:
                break
            if length == rit - lft + 1:
                ans += 1
        freq[a[lft]] -= 1
    print(ans)


if __name__ == '__main__':
    import sys

    sys.stdin = open(r'C:\rocky_d\code\informatics\code\py\src\draft\in.txt')
    for _ in range(int(input())):
        main()
