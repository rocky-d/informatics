def main() -> None:
    n = int(input())

    ans = []
    i = 2
    while i <= n // i:
        if 0 == n % i:
            cnt = 0
            while 0 == n % i:
                n //= i
                cnt += 1
            if 1 == cnt:
                ans.append(str(i))
            else:
                ans.append(str(i) + '^' + str(cnt))
        i += 1
    if 1 < n:
        ans.append(str(n))
    print(*ans, sep = ' * ')


if __name__ == '__main__':
    main()
