from collections import deque


def main() -> None:
    n = int(input())
    gaps = input().split()
    m = int(input())
    fills = [input().split()[1:] for _ in range(m)]

    ans = deque(maxlen = m)

    def dfs(index: int) -> bool:
        if index == n - 1:
            return True
        for i, fill in enumerate(fills, 1):
            if fill == gaps[index:index + len(fill)]:
                ans.append(i)
                if dfs(index + len(fill) - 1):
                    res = True
                    break
                ans.pop()
        else:
            res = False
        return res

    dfs(0)
    print(*ans)


if __name__ == '__main__':
    main()
