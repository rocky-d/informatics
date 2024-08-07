from math import comb


def main() -> None:
    n = int(input())
    s = input()

    if 0b1 == 0b1 & n:
        print(0)
        return
    lfts = rits = n // 2
    for char in s:
        if '(' == char:
            lfts -= 1
        elif ')' == char:
            rits -= 1
    x, y = (lfts, rits) if lfts < rits else (rits, lfts)
    if x < 0:
        print(0)
        return
    if x == 0:
        print(1)
        return
    print(comb(x + y, x) % 1_000_000_007)


if __name__ == '__main__':
    main()
