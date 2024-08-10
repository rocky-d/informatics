def main() -> None:
    w, d = map(int, input().split())
    pa = (map(int, input().split()) for _ in range(w))

    prime_factors = {}
    for p, a in pa:
        prime_factors[p] = a


if __name__ == '__main__':
    main()
