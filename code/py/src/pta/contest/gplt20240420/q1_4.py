def main():
    n, m = map(int, input().split())
    k = map(int, input().split())

    total = sum(k)
    ans = max(0, total - (n * (m - 1)))
    print(ans)


if __name__ == '__main__':
    main()
