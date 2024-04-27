def main() -> None:
    n = int(input())
    rules = (
        '2(0)', '2', '2(2)',
        '2(2+2(0))', '2(2(2))', '2(2(2)+2(0))',
        '2(2(2)+2)', '2(2(2)+2+2(0))', '2(2(2+2(0)))',
        '2(2(2+2(0))+2(0))', '2(2(2+2(0))+2)', '2(2(2+2(0))+2+2(0))',
        '2(2(2+2(0))+2(2))', '2(2(2+2(0))+2(2)+2(0))', '2(2(2+2(0))+2(2)+2)',
    )
    ans = []
    n_bin = bin(n)[2:]
    for i in range(-1, -1 - len(n_bin), -1):
        if '1' == n_bin[i]:
            ans.insert(0, rules[-i - 1])
    print('+'.join(ans))


if __name__ == '__main__':
    main()
