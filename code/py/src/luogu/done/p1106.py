def main() -> None:
    n_ls = [int(ch) for ch in input().strip()]
    for _ in range(int(input())):
        for i in range(len(n_ls) - 1):
            if n_ls[i] > n_ls[i + 1]:
                del n_ls[i]
                break
        else:
            del n_ls[-1]
        while len(n_ls) > 0 and n_ls[0] == 0:
            del n_ls[0]
    print(''.join(map(str, n_ls)) if len(n_ls) > 0 else '0')


if __name__ == '__main__':
    main()
