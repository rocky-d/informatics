from functools import cache


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = list(a)

    @cache
    def dfs(lft: int, rit: int, lst: int) -> bool:
        if not lft <= rit:
            return False
        return lst < a[lft] and not dfs(lft + 1, rit, a[lft]) or lst < a[rit] and not dfs(lft, rit - 1, a[rit])

    print('Alice' if dfs(lft=0, rit=n - 1, lst=0) else 'Bob')


if __name__ == '__main__':
    main()
