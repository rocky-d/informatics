def main():
    n = int(input())
    a = map(int, input().split())

    a = list(a)
    print(sum((a[i] ^ a[j]) * (j - i) for i in range(n) for j in range(i + 1, n)))


main()
