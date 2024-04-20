def main():
    n, c = input().split()
    n = int(n)

    row = n * c
    for _ in range((n + 1) // 2):
        print(row)


if __name__ == "__main__":
    main()
