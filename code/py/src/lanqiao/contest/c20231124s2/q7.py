def main() -> None:
    letters = ('a', 'e', 'i', 'o', 'u')
    s = input()
    for ch in s[::-1]:
        if ch in letters:
            print(ch)
            break


if __name__ == '__main__':
    main()
