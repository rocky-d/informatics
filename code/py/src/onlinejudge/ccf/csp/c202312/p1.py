def main() -> None:
    n, m = map(int, input().split())
    houses = (map(int, input().split()) for _ in range(n))

    ans = []
    houses = list(enumerate(map(tuple, houses), start=1))
    for i, ai in houses:
        for j, aj in houses:
            if all(x < y for x, y in zip(ai, aj)):
                ans.append(j)
                break
        else:
            ans.append(0)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
