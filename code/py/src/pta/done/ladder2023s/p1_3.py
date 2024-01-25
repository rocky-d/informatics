def main() -> None:
    a, b = map(int, input().split())
    x, y = max(0, a, b), max(0, a + b)
    ans = '^_^' if x < y else 'T_T' if y < x else '-_-'
    print(x, y)
    print(ans)


if __name__ == '__main__':
    main()
