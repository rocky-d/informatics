def main() -> None:
    ans = 0
    for i, digit in zip(range(4), reversed((2, 0, 2, 2))):
        ans += digit * 9 ** i
    print(ans)


if __name__ == '__main__':
    main()
