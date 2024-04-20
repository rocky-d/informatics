def count(s: str) -> int:
    res = 0
    for ch in s:
        res += int(ch)
    return res


def main() -> None:
    cnt = 0
    for i in range(1, 10000000000000000000000000):
        if count(str(oct(i))[2:]) == count(str(bin(i))[2:]):
            print(i)
            cnt += 1
            if 23 == cnt:
                break


if __name__ == '__main__':
    main()
