from collections import Counter


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    cnter = Counter(ai for ai in a if 0 <= ai)
    for num in list(cnter.keys()):
        if 0b0 == 0b1 & cnter[num]:
            del cnter[num]
    ps, ns = len(cnter), sum(1 for ai in a if ai < 0)
    print(0b1 & (ns - ps) if ps < ns else ps - ns)


if __name__ == '__main__':
    main()
