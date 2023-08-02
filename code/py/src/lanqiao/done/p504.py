def main():
    s = input().strip()
    table = {ch: 0 for ch in 'abcdefghijklmnopqrstuvwxyz'}
    for ch in s:
        table[ch] += 1
    res = ['', -1]
    for item in table.items():
        if item[1] > res[1]:
            res[0] = item[0]
            res[1] = item[1]
    print(res[0])
    print(res[1])


if __name__ == '__main__':
    main()
