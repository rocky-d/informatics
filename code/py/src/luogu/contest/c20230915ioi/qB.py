def main() -> None:
    n, m, p, q = map(int, input().strip().split())
    nm = n * m
    index = p * m + q

    if -1 < index < nm:
        print('Program ends with return value 0.')
    else:
        print('Segmentation fault.')


if __name__ == '__main__':
    main()
