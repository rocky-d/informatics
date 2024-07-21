from collections import Counter


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    cnter = Counter(ai for ai in a if 0 <= ai)
    for num in list(cnter.keys()):
        cnter[num] %= 2
        if 0 == cnter[num]:
            del cnter[num]
    ns = sum(1 for ai in a if ai < 0)
    ps = len(cnter)
    if ps >= ns:
        print(ps - ns)
    else:
        print(0b1 & (ns - ps))


if __name__ == '__main__':
    main()
