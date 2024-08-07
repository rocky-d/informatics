from functools import lru_cache
from itertools import accumulate


@lru_cache(maxsize = None)
def dfs(num: int) -> int:
    if 0 == num:
        return 0
    return 1 + dfs(num // 3)


prefs = list(accumulate((dfs(num = num) for num in range(200_001)), initial = 0))


def main() -> None:
    l, r = map(int, input().split())

    print(dfs(num = l) + prefs[r + 1] - prefs[l])


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
