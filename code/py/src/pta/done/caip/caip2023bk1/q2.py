from collections import deque


def main() -> None:
    n, m = map(int, input().split())
    known = (input().split() for _ in range(n))
    unknown = (input() for _ in range(m))

    ans = []
    dct = {name: level for name, level in known}
    level = ''
    stk = deque()

    def dfs(name: str) -> int:
        nonlocal level
        if '' == name:
            level = ''.join(stk)
            return 1 if 2 == len(stk) else 0
        cnt = 0
        s = ''
        for i, char in enumerate(name, start = 1):
            s += char
            if s in dct.keys():
                stk.append(dct[s])
                cnt += dfs(name[i:])
                stk.pop()
        return cnt

    for name in unknown:
        if name in dct.keys():
            ans.append(dct[name])
        else:
            if 1 == dfs(name = name):
                ans.append(level)
            else:
                ans.append('D')
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
