def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    a = list(a)
    maxm = max(a)
    for i in range(maxm, maxm + k + 1):
        if all(0b0 == 0b1 & (i - ai) // k for ai in a):
            ans = i
            break
    else:
        ans = -1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
