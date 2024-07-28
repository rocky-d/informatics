def main() -> None:
    s = input()

    print(sum(diff if diff < 13 else 26 - diff for diff in (abs(si - ti) for si, ti in zip(map(ord, s), map(ord, s[::-1])))) // 2)


if __name__ == '__main__':
    main()
