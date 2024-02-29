def main() -> None:
    ans = 0
    for lft in range(0, 101):
        for rit in range(lft + 10, 101):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
