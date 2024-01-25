from math import log2


def main() -> None:
    dice = list(map(int, input().split()))
    n = int(input())
    dice_s = list(0b1 << (6 - die) for die in dice)
    for _ in range(n):
        for i in range(6):
            p = 0b1
            while True:
                if 0b0 == p & dice_s[i]:
                    dice_s[i] |= p
                    dice[i] = 6 - int(log2(p))
                    break
                p <<= 1
    print(*dice)


if __name__ == '__main__':
    main()
