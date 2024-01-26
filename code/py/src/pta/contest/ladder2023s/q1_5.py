def main() -> None:
    dice = list(map(int, input().split()))
    n = int(input())

    dice_s = list(0b1 << die for die in dice)
    for _ in range(n):
        for j in range(6):
            for k in range(6, 0, -1):
                if 0b0 == 0b1 & (dice_s[j] >> k):
                    dice_s[j] |= 0b1 << k
                    dice[j] = k
                    break
    print(*dice)


if __name__ == '__main__':
    main()
