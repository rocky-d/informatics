from itertools import combinations
from math import gcd


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = set(a)
    addition = set()

    def dfs() -> bool:
        res = False
        for num1, num2 in combinations(a, r = 2):
            x = gcd(num1, num2)
            if x in a:
                continue
            a.add(x)
            addition.add(x)
            nxt = dfs()
            a.remove(x)
            if not nxt:
                res = True
                # break
        return res

    print('dXqwq' if dfs() else 'Haitang')
    print(addition)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
