from heapq import heappop, heappush


def case() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    heap_max = [(-a[0], 0)]
    cnt = 0
    for _ in range(k):
        item = heappop(heap_max)
        ai, i = -item[0], -item[1]
        if cnt == i:
            cnt += 1
            if cnt < n:
                heappush(heap_max, (-a[cnt], -cnt))
        ans += ai
        heappush(heap_max, (-b[i], -i))
    print(ans)


def main() -> None:
    for _ in range(int(input())):
        case()


if __name__ == '__main__':
    main()
