from heapq import heapify, heappop, heappush
from operator import neg


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0
    ab = list(zip(map(neg, a), b))
    heapify(ab)
    for _ in range(k):
        ai, bi = heappop(ab)
        ans -= ai
        heappush(ab, (min(0, ai + bi), bi))
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
