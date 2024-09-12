def main() -> None:
    n = int(input())

    ls = [0] * (1 + n)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        ls[a] += 1
        ls[b] += 1
    print(sum(1 for i in range(1, n + 1) if 1 == ls[i]))


if __name__=='__main__':
    for _ in range(int(input())):
        main()
