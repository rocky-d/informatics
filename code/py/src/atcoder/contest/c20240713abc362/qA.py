def main() -> None:
    r, g, b = map(int, input().split())
    c = input()

    c = c[0]
    if 'R' == c:
        ans = min(g, b)
    elif 'G' == c:
        ans = min(r, b)
    else:  # 'B' == c:
        ans = min(r, g)
    print(ans)


if __name__ == '__main__':
    main()
