def main() -> None:
    a = int(input())

    if 1 == a:
        print(0b10, 0b11)
        return
    if 1 == bin(a)[2:].count('1'):
        print(0b1, 0b1 | a)
        return
    mask = 0b1 << a.bit_length() - 1
    print(mask | 0b0, ~mask & a)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
