def main() -> None:
    ans = 0
    for i in range(1, 2024):
        if 0 == 2023 % i:
            ans += 1
            print(i)
    print(ans)


if __name__ == '__main__':
    main()
