def main() -> None:
    a, b = map(int, input().split())
    if 0 < a and 0 < b:
        ans = f"{max(a, b)} {a + b}\n^_^"
    elif a < 0 and b < 0:
        ans = '0 0\n-_-'
    else:
        ans = f"{max(a, b)} {max(0, a + b)}\nT_T"
    print(ans)


if __name__ == '__main__':
    main()
