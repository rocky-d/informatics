def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = (map(int, input().split()) for _ in range(n))

    nutrients = [0] * m
    for xi in x:
        for j, xij in enumerate(xi):
            nutrients[j] += xij
    print('Yes' if all(a[i] <= nutrients[i] for i in range(m)) else 'No')


if __name__ == '__main__':
    main()
