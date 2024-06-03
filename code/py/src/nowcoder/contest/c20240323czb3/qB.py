from collections import deque


def main() -> None:
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    q = int(input())
    queries = (map(int, input().split()) for _ in range(q))

    ans = deque()
    prefs = [0]
    lst = 0
    for ai, bi in zip(a, b):
        if ai == bi:
            lst += 1
        prefs.append(lst)
    for l, r in queries:
        ans.append('YES' if 0 == prefs[r] - prefs[l - 1] else 'NO')
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
