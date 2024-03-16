from bisect import insort
from collections import deque, Counter


def main() -> None:
    n, m = map(int, input().split())
    num_x = deque(maxlen = n)
    x = deque(maxlen = n)
    for i in range(n):
        num_x.append(int(input()))
        x.append(map(int, input().split()))
    num_y = deque(maxlen = m)
    y = deque(maxlen = m)
    for _ in range(m):
        num_y.append(int(input()))
        y.append(map(int, input().split()))

    ans = []
    ans_x = []
    cnter = Counter()
    for len_x, xi in zip(num_x, x):
        for val in xi:
            cnter[val] += 1
            if len_x < 2 * cnter[val]:
                insort(ans, val)
                insort(ans_x, val)
                break
        else:
            insort(ans, 5)
            insort(ans_x, 5)
        cnter.clear()
    ans_y = []
    cnter = Counter()
    for len_y, yi in zip(num_y, y):
        for val in yi:
            cnter[val] += 1
            if len_y < 2 * cnter[val]:
                insort(ans, val)
                insort(ans_y, val)
                break
        else:
            insort(ans, 5)
            insort(ans_y, 5)
        cnter.clear()
    print(*ans_x)
    print(*ans_y)
    print((ans[(n + m) // 2] + ans[(n + m) // 2 - 1]) // 2 if 0 == (n + m) % 2 else ans[(n + m) // 2])


if __name__ == '__main__':
    main()
