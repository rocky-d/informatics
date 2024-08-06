def main() -> None:
    s = input()
    t = input()

    chars = ['a' if '?' == char else char for char in s]
    ti, m = 0, len(t)
    for si, char in enumerate(s):
        if t[ti] == char:
            ti += 1
        elif '?' == char:
            chars[si] = t[ti]
            ti += 1
        else:
            continue
        if ti == m:
            break
    else:
        print('NO')
        return
    print('YES')
    print(''.join(chars))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
