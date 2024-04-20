def main() -> None:
    for _t in range(int(input())):
        n = int(input())
        s = input()
        print('YES' if n == len('Timur') and set(list(s)) == set(list('Timur')) else 'NO')


if __name__ == '__main__':
    main()
