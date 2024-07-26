def main() -> None:
    n, x = map(int, input().split())

    ans = 0
    for a in range(1, x - 1):
        for b in range(1, x - a):
            tmp = (n - a * b) // (a + b)
            if 0 < tmp:
                ans += min(x - a - b, tmp)
            else:
                break
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()

'''
c <= x-a-b
c <= (n-ab)/(a+b)
'''
