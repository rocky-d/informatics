def main() -> None:
    s = input()
    len_s = len(s)
    if 0 == len_s % 3:
        index = 2 * len_s // 3
        ans = s[:index] + ' ' + s[index:]
    else:
        ans = '-1'
    print(ans)


if __name__ == '__main__':
    main()
