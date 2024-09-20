def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a_set = frozenset(a)
    if 1 not in a_set:
        print(0)
        return
    ans = 0
    a = sorted(a_set)
    tags = [None] + [True] * a[-1]
    for num in range(1, a[-1] + 1):
        if num in a_set:
            if tags[num]:
                ans += 1
        else:  # elif num not in a_set:
            for comp in range(num, a[-1] + 1, num):
                tags[comp] = False
    print(ans)


if __name__ == '__main__':
    main()
