def main() -> None:
    n, m = map(int, input().split())
    ab = (input().split() for _ in range(m))

    ans = []
    families = [None] + [True] * n
    for a, b in ab:
        a = int(a)
        if families[a] and 'M' == b:
            families[a] = False
            ans.append('Yes')
        else:
            ans.append('No')
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
