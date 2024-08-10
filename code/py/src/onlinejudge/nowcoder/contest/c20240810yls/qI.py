def main() -> None:
    s = 'today'
    t = 'xishi'

    cnts = 0
    for char in s:
        print(ord(char))
        cnts += ord(char)
    print()
    cntt = 0
    for char in t:
        print(ord(char))
        cntt += ord(char)
    print(cnts - cntt)


if __name__ == '__main__':
    main()
