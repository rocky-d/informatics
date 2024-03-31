def main() -> None:
    s = input()

    s = s[3:] + s[:3]
    ans = []
    for char in s:
        ans.append(str(ord(char)))
    print(''.join(ans))


if __name__ == '__main__':
    main()
