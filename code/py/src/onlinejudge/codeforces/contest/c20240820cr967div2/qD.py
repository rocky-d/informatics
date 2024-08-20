from collections import defaultdict
from itertools import groupby


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    ans = []
    a = [ai for ai, group in groupby(a)]
    print(a)
    idxes = defaultdict(lambda: [])
    for i, ai in enumerate(a):
        idxes[ai].append(i)
    vis = set()
    unvis = set(a)
    idx = 0

    def bi1() -> int:
        def check1() -> bool:
            ...

    def bi2() -> int:
        def check2() -> bool:
            ...

    for i in range(len(unvis)):
        if 0b0 == 0b1 & i:
            res = bi1()
        else:
            res = bi2()
        idx = res + 1
        ans.append(a[res])


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
