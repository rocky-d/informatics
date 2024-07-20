from collections import Counter


def main() -> None:
    n, k = map(int, input().split())
    s = input()

    cnter = Counter(s)
    ls = [''] * n

    def dfs(idx: int) -> int:
        if idx == n:
            return 1
        res = 0
        nxt = idx + 1
        lft = nxt - k
        if lft < 0:
            for char in cnter.keys():
                if 0 == cnter[char]:
                    continue
                ls[idx] = char
                cnter[char] -= 1
                res += dfs(nxt)
                cnter[char] += 1
        else:
            for char in cnter.keys():
                if 0 == cnter[char]:
                    continue
                ls[idx] = char
                if all(ls[y] == ls[idx - x] for x, y in enumerate(range(lft, lft + k // 2 + 1))):
                    continue
                cnter[char] -= 1
                res += dfs(nxt)
                cnter[char] += 1
        return res

    print(dfs(idx = 0))


if __name__ == '__main__':
    main()
