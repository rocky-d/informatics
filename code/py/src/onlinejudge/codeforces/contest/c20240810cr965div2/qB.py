from collections import deque


def main() -> None:
    n = int(input())
    p = map(int, input().split())

    p = deque(p)
    p.appendleft(p.pop())
    print(*p)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
