def main() -> None:
    for _t in range(int(input())):
        s = input()
        s_tuple = tuple(set(s))
        print('Yes' if len(s_tuple) == 2 and s.count(s_tuple[0]) in (1, 3) else 'No')


if __name__ == '__main__':
    main()
