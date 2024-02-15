def main() -> None:
    s = input()

    dp = [0, 0, 0]
    for char in s:
        dp.append(max(dp[-1], max(dp[-2], dp[-3]) + ord(char) - ord('a') + 1))
    print(dp[-1])


if __name__ == '__main__':
    main()
