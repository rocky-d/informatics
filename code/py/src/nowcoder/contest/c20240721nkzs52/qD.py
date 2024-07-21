from heapq import heapify, heappop, heappush


def main() -> None:
    n = int(input())
    a = input().split()

    ans = ''
    heap = list(list(-int(char) for char in ai) + [1] for ai in a)
    heapify(heap)
    while 0 < len(heap):
        ls = heappop(heap)
        ans += str(-ls.pop(0))
        if 1 < len(ls):
            heappush(heap, ls)
    print(ans)


if __name__ == '__main__':
    main()
