from collections import deque


def main() -> None:
    n, k = map(int, input().split())
    r = map(int, input().split())

    ans = []
    r = list(r)
    stk = deque()

    def dfs(i: int, total: int) -> None:
        if i == n:
            if 0 == total % k:
                ans.append(' '.join(map(str, stk)))
            return
        for ai in range(1, r[i] + 1):
            stk.append(ai)
            dfs(i + 1, total + ai)
            stk.pop()

    dfs(i = 0, total = 0)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
