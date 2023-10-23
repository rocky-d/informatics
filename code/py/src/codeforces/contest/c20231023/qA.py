def main() -> None:
    input()
    a_ls = list(map(int, input().split()))
    b_ls = []
    for a in a_ls:
        b_ls.append(a - 1 if 0 == a % 2 else a)
    print(*b_ls)


if __name__ == '__main__':
    main()
